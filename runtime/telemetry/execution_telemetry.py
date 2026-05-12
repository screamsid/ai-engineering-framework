from datetime import datetime, UTC


class ExecutionTelemetry:
    """Collect lightweight runtime execution telemetry.

    Telemetry must remain operationally useful.
    It should support debugging, calibration, and governance improvement,
    not vanity metrics.
    """

    def build_event(
        self,
        task: dict,
        adapter_result: dict,
        validation_result: dict,
        confidence_result: dict,
        calibration_result: dict,
        token_estimate: dict | None = None,
    ) -> dict:
        return {
            "timestamp": datetime.now(UTC).isoformat(),
            "task_id": task.get("id"),
            "task_type": task.get("type"),
            "adapter": adapter_result.get("adapter", {}).get("name"),
            "execution_success": adapter_result.get("execution", {}).get("success"),
            "validation_passed": validation_result.get("passed"),
            "confidence_score": confidence_result.get("confidence_score"),
            "human_validation_required": confidence_result.get(
                "human_validation_required"
            ),
            "calibration_state": calibration_result.get("validation_result"),
            "adjusted_confidence": calibration_result.get(
                "adjusted_confidence"
            ),
            "estimated_tokens": (
                token_estimate or {}
            ).get("estimated_tokens"),
            "token_warning": (
                token_estimate or {}
            ).get("warning"),
        }
