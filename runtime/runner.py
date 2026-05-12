from pathlib import Path
import yaml

from runtime.loaders.role_loader import RoleLoader
from runtime.loaders.skill_loader import SkillLoader
from runtime.loaders.context_assembler import ContextAssembler
from runtime.gates.confidence_gate import ConfidenceGate
from runtime.validators.basic_validator import RuntimeValidator
from runtime.formatters.human_formatter import HumanFormatter
from runtime.audit.audit_logger import AuditLogger
from runtime.calibration.calibration_engine import CalibrationEngine
from runtime.calibration.store import CalibrationStore
from runtime.router.router import RuntimeRouter


class RuntimeRunner:
    """Minimal runtime orchestration prototype.

    Prototype boundary:
    - this runner does not yet invoke a real external agent
    - validation currently uses a clearly marked stub output
    - agent adapter integration is the next runtime maturity step
    """

    def __init__(self):
        self.role_loader = RoleLoader()
        self.skill_loader = SkillLoader()
        self.context_assembler = ContextAssembler()
        self.confidence_gate = ConfidenceGate()
        self.validator = RuntimeValidator()
        self.formatter = HumanFormatter()
        self.audit_logger = AuditLogger()
        self.calibration_engine = CalibrationEngine()
        self.calibration_store = CalibrationStore()
        self.router = RuntimeRouter()

    def load_task(self, task_file: str) -> dict:
        task_path = Path(task_file)

        with open(task_path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)

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

        runtime_context = self.context_assembler.assemble(
            role_card=role_card,
            skills=skills,
            task=task,
        )

        confidence_thresholds = role_card.get(
            "confidence", {}
        ).get("minimum_autonomous_score", {})

        confidence_result = self.confidence_gate.evaluate(
            confidence_score=task["runtime"]["confidence_score"],
            risk_level=task["runtime"]["risk_level"],
            thresholds=confidence_thresholds,
        )

        # PROTOTYPE STUB ONLY.
        # This is not real agent output.
        # Replace this with adapter output once runtime/adapters exists.
        # The explicit stub prevents false confidence about current runtime maturity.
        sample_output = """
## Implementation Summary
Runtime executed successfully.

## Validation Summary
Validation completed.

## Confidence Gate
Confidence: 92%
Risk Level: Low

## Known Gaps
No live agent execution yet.

## Handoff
Ready for review.
"""

        validation_result = self.validator.validate(
            sample_output
        )

        calibration_result = self.calibration_engine.adjust(
            original_confidence=task["runtime"][
                "confidence_score"
            ],
            validation_result="approved",
        )

        self.calibration_store.save(
            calibration_result
        )

        runtime_result = {
            "task": task.get("task", {}),
            "routing_decision": routing_decision,
            "runtime_context": runtime_context,
            "confidence_result": confidence_result,
            "validation_result": validation_result,
            "calibration_result": calibration_result,
            "prototype_limits": [
                "No real external agent invocation yet",
                "Validation uses explicit stub output",
                "Agent adapter layer not implemented yet",
            ],
        }

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
