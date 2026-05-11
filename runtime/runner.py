from pathlib import Path
import yaml

from runtime.loaders.role_loader import RoleLoader
from runtime.loaders.skill_loader import SkillLoader
from runtime.loaders.context_assembler import ContextAssembler
from runtime.gates.confidence_gate import ConfidenceGate


class RuntimeRunner:
    """Minimal runtime orchestration prototype."""

    def __init__(self):
        self.role_loader = RoleLoader()
        self.skill_loader = SkillLoader()
        self.context_assembler = ContextAssembler()
        self.confidence_gate = ConfidenceGate()

    def load_task(self, task_file: str) -> dict:
        task_path = Path(task_file)

        with open(task_path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)

    def run(self, task_file: str) -> dict:
        task = self.load_task(task_file)

        role_name = task["runtime"]["role"]

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

        return {
            "task": task.get("task", {}),
            "runtime_context": runtime_context,
            "confidence_result": confidence_result,
        }


if __name__ == "__main__":
    runner = RuntimeRunner()

    result = runner.run(
        "examples/runtime-task.yaml"
    )

    print(result)
