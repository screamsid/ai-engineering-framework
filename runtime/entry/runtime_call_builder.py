import yaml


REQUIRED_FIELDS = [
    "task_id",
    "task_type",
    "objective",
    "scope",
    "risk_level",
    "confidence_score",
    "validation_requirements",
    "stop_conditions",
]


class RuntimeCallBuilder:
    """Build minimal valid RUNTIME-CALL.yaml files from human input."""

    def validate(self, task_input: dict) -> list:
        issues = []

        for field in REQUIRED_FIELDS:
            if not task_input.get(field):
                issues.append(
                    f"Missing required field: {field}"
                )

        risk_level = task_input.get("risk_level")

        if risk_level and risk_level not in [
            "low",
            "medium",
            "high",
            "critical",
        ]:
            issues.append(
                "Invalid risk level"
            )

        confidence = task_input.get(
            "confidence_score",
            0,
        )

        if not isinstance(confidence, int):
            issues.append(
                "Confidence score must be an integer"
            )

        elif confidence < 0 or confidence > 100:
            issues.append(
                "Confidence score must be between 0 and 100"
            )

        return issues

    def build(self, task_input: dict) -> dict:
        issues = self.validate(task_input)

        if issues:
            raise ValueError(
                f"Invalid task input: {issues}"
            )

        return {
            "version": "0.3.1",
            "task": {
                "id": task_input["task_id"],
                "type": task_input["task_type"],
                "objective": task_input["objective"],
                "scope": task_input["scope"],
                "out_of_scope": task_input.get(
                    "out_of_scope",
                    [],
                ),
            },
            "governance": {
                "risk_level": task_input["risk_level"],
                "confidence_score": task_input[
                    "confidence_score"
                ],
                "confidence_threshold": task_input.get(
                    "confidence_threshold",
                    85,
                ),
                "mode": task_input.get(
                    "mode",
                    "standard",
                ),
                "preset": task_input.get(
                    "preset",
                    task_input["task_type"],
                ),
            },
            "required_outputs": [
                "implementation_summary",
                "validation_summary",
                "confidence_gate",
                "known_gaps",
                "handoff",
            ],
            "stop_conditions": task_input[
                "stop_conditions"
            ],
            "validation": {
                "required_tests": task_input[
                    "validation_requirements"
                ],
                "success_criteria": task_input.get(
                    "success_criteria",
                    [],
                ),
            },
        }

    def to_yaml(self, runtime_call: dict) -> str:
        return yaml.safe_dump(
            runtime_call,
            sort_keys=False,
        )
