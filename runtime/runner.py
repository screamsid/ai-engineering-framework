from pathlib import Path
import yaml

from runtime.loaders.role_loader import RoleLoader
from runtime.loaders.skill_loader import SkillLoader
from runtime.loaders.context_assembler import ContextAssembler
from runtime.compiler.context_compiler import ContextCompiler
from runtime.memory.memory_loader import MemoryLoader
from runtime.tokens.token_estimator import TokenEstimator
from runtime.telemetry.execution_telemetry import (
    ExecutionTelemetry,
)
from runtime.gates.confidence_gate import ConfidenceGate
from runtime.validators.basic_validator import RuntimeValidator
from runtime.formatters.human_formatter import HumanFormatter
from runtime.audit.audit_logger import AuditLogger
from runtime.calibration.calibration_engine import CalibrationEngine
from runtime.calibration.store import CalibrationStore
from runtime.router.router import RuntimeRouter
from runtime.adapters.registry import AdapterRegistry


class RuntimeRunner:
    """Minimal runtime orchestration prototype.

    Prototype boundary:
    - this runner invokes adapters through the adapter registry
    - the default safe adapter is the mock adapter
    - real external agent adapters are scaffolded but not implemented yet
    """

    def __init__(self):
        self.role_loader = RoleLoader()
        self.skill_loader = SkillLoader()
        self.context_assembler = ContextAssembler()
        self.context_compiler = ContextCompiler()
        self.memory_loader = MemoryLoader(
            memory_items=[
                {
                    "id": "memory-001",
                    "content": "Prefer small safe changes.",
                    "applies_to": [
                        "python-automation",
                    ],
                    "risk_scope": [
                        "low",
                        "medium",
                    ],
                }
            ]
        )
        self.token_estimator = TokenEstimator()
        self.execution_telemetry = (
            ExecutionTelemetry()
        )
        self.confidence_gate = ConfidenceGate()
        self.validator = RuntimeValidator()
        self.formatter = HumanFormatter()
        self.audit_logger = AuditLogger()
        self.calibration_engine = CalibrationEngine()
        self.calibration_store = CalibrationStore()
        self.router = RuntimeRouter()
        self.adapter_registry = AdapterRegistry()

    def load_task(self, task_file: str) -> dict:
        task_path = Path(task_file)

        with open(task_path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)

    def build_adapter_payload(
        self,
        task: dict,
        runtime_context: dict,
        routing_decision: dict,
        confidence_result: dict,
    ) -> dict:
        return {
            "task": task.get("task", {}),
            "runtime_context": runtime_context,
            "routing_decision": routing_decision,
            "governance": {
                "confidence_score": task["governance"][
                    "confidence_score"
                ],
                "human_validation_required": confidence_result[
                    "human_validation_required"
                ],
                "required_outputs": runtime_context.get(
                    "required_outputs", []
                ),
            },
        }

    def adapter_output_to_markdown(
        self,
        adapter_result: dict,
    ) -> str:
        output = adapter_result.get("output", {})

        known_gaps = "\n".join(
            f"- {gap}"
            for gap in output.get("known_gaps", [])
        )

        return f"""
## Implementation Summary
{output.get('implementation_summary', '')}

## Validation Summary
{output.get('validation_summary', '')}

## Confidence Gate
{output.get('confidence_gate', '')}

## Known Gaps
{known_gaps}

## Handoff
{output.get('handoff', '')}
"""

    def run(self, task_file: str) -> dict:
        task = self.load_task(task_file)

        self.audit_logger.write(
            f"Starting task: {task.get('task', {}).get('id')}"
        )

        routing_decision = self.router.route(task)

        role_name = routing_decision[
            "assignment"
        ].get("role", "builder")

        role_card = self.role_loader.load(role_name)

        skills = []

        for skill_name in role_card.get(
            "required_skills", []
        ):
            try:
                skills.append(
                    self.skill_loader.load(skill_name)
                )
            except FileNotFoundError:
                pass

        memory_items = self.memory_loader.load_relevant(
            task_type=task["task"]["type"],
            risk_level=task["governance"][
                "risk_level"
            ],
        )

        runtime_context = self.context_assembler.assemble(
            role_card=role_card,
            skills=skills,
            task=task,
            memory_items=memory_items,
        )

        compiled_context = self.context_compiler.compile(
            runtime_context
        )

        confidence_thresholds = role_card.get(
            "confidence", {}
        ).get("minimum_autonomous_score", {})

        confidence_result = self.confidence_gate.evaluate(
            confidence_score=task["governance"][
                "confidence_score"
            ],
            risk_level=task["governance"][
                "risk_level"
            ],
            thresholds=confidence_thresholds,
        )

        preferred_agent = routing_decision["assignment"].get(
            "preferred_agent",
            "mock",
        )

        adapter_name = task.get("routing", {}).get(
            "adapter",
            "mock",
        )

        if adapter_name == "preferred":
            adapter_name = preferred_agent

        adapter = self.adapter_registry.get(adapter_name)

        adapter_payload = self.build_adapter_payload(
            task=task,
            runtime_context=compiled_context,
            routing_decision=routing_decision,
            confidence_result=confidence_result,
        )

        token_estimate = (
            self.token_estimator.estimate_payload(
                adapter_payload
            )
        )

        adapter_result = adapter.invoke(adapter_payload)

        adapter_markdown = self.adapter_output_to_markdown(
            adapter_result
        )

        validation_result = self.validator.validate(
            adapter_markdown
        )

        calibration_state = (
            "approved"
            if validation_result["passed"]
            else "rejected"
        )

        calibration_result = self.calibration_engine.adjust(
            original_confidence=task["governance"][
                "confidence_score"
            ],
            validation_result=calibration_state,
        )

        self.calibration_store.save(
            calibration_result
        )

        telemetry_event = (
            self.execution_telemetry.build_event(
                task=task.get("task", {}),
                adapter_result=adapter_result,
                validation_result=validation_result,
                confidence_result=confidence_result,
                calibration_result=calibration_result,
                token_estimate=token_estimate,
            )
        )

        runtime_result = {
            "task": task.get("task", {}),
            "routing_decision": routing_decision,
            "runtime_context": runtime_context,
            "compiled_context": compiled_context,
            "confidence_result": confidence_result,
            "adapter_result": adapter_result,
            "validation_result": validation_result,
            "calibration_state": calibration_state,
            "calibration_result": calibration_result,
            "token_estimate": token_estimate,
            "telemetry_event": telemetry_event,
            "prototype_limits": [
                "Default execution uses mock adapter unless configured otherwise",
                "Real external agent adapters are scaffolded but not implemented yet",
            ],
        }

        if token_estimate.get("warning"):
            runtime_result[
                "token_warning"
            ] = (
                "Estimated token count exceeds recommended threshold"
            )

        human_output = self.formatter.format(
            runtime_result
        )

        self.audit_logger.write(
            f"Completed task: {task.get('task', {}).get('id')}"
        )

        return {
            "runtime_result": runtime_result,
            "human_output": human_output,
        }


if __name__ == "__main__":
    runner = RuntimeRunner()

    result = runner.run(
        "examples/runtime-task.yaml"
    )

    print(result)
