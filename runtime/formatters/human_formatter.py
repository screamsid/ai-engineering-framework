class HumanFormatter:
    """Convert structured runtime output into human-readable form without changing meaning."""

    def format(self, runtime_result: dict) -> str:
        task = runtime_result.get("task", {})
        confidence = runtime_result.get(
            "confidence_result", {}
        )

        return (
            f"Task: {task.get('objective')}\n"
            f"Risk Level: {confidence.get('risk_level')}\n"
            f"Confidence Score: {confidence.get('confidence_score')}\n"
            f"Required Threshold: {confidence.get('required_score')}\n"
            f"Approved: {confidence.get('approved')}\n"
            f"Human Validation Required: "
            f"{confidence.get('human_validation_required')}"
        )
