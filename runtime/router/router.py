from pathlib import Path
import yaml


class RuntimeRouter:
    """Deterministic-first runtime router."""

    def __init__(
        self,
        rules_path: str = "runtime/router/routing-rules.yaml",
    ):
        self.rules_path = Path(rules_path)

        with open(self.rules_path, "r", encoding="utf-8") as handle:
            self.rules = yaml.safe_load(handle)

    def route(self, task: dict) -> dict:
        risk_level = task["governance"]["risk_level"]

        decision = {
            "task": {
                "type": task["task"]["type"],
                "risk_level": risk_level,
            },
            "assignment": {},
            "governance": {
                "reviewer_required": False,
                "security_review_required": False,
                "human_validation_required": False,
            },
            "confidence": {
                "routing_confidence": 95,
                "rationale": "Matched deterministic routing rules",
            },
        }

        for rule in self.rules.get("routing_rules", []):
            match = rule.get("match", {})
            assign = rule.get("assign", {})

            task_type_match = (
                "task_type" not in match
                or match["task_type"] == task["task"]["type"]
            )

            risk_match = (
                "risk_level" not in match
                or match["risk_level"] == risk_level
            )

            if task_type_match and risk_match:
                for key, value in assign.items():
                    if key in decision["assignment"]:
                        decision["assignment"][key] = value
                    elif key in decision["governance"]:
                        decision["governance"][key] = value
                    else:
                        decision["assignment"][key] = value

        return decision
