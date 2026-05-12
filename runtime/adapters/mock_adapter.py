from runtime.adapters.base_adapter import BaseAdapter


class MockAdapter(BaseAdapter):
    """Mock adapter for testing runtime execution without external agents.

    This adapter intentionally avoids API calls, CLI execution, token usage,
    and filesystem changes. It exists to validate the runtime lifecycle.
    """

    adapter_name = "mock"

    def invoke(self, runtime_payload: dict) -> dict:
        task = runtime_payload.get("task", {})
        governance = runtime_payload.get("governance", {})

        confidence_score = governance.get(
            "confidence_score",
            90,
        )

        human_validation_required = governance.get(
            "human_validation_required",
            False,
        )

        return {
            "adapter": {
                "name": self.adapter_name,
                "version": "0.1.0",
            },
            "execution": {
                "success": True,
                "execution_time_ms": 0,
                "token_estimate": 0,
            },
            "output": {
                "implementation_summary": (
                    f"Mock execution completed for task: "
                    f"{task.get('objective')}"
                ),
                "validation_summary": (
                    "Mock validation completed successfully."
                ),
                "confidence_gate": (
                    f"Confidence: {confidence_score}%"
                ),
                "known_gaps": [
                    "Mock adapter does not execute external agents.",
                    "No real code changes are performed.",
                ],
                "handoff": "Ready for runtime review.",
            },
            "governance": {
                "confidence_score": confidence_score,
                "human_validation_required": human_validation_required,
            },
            "errors": [],
        }
