from runtime.runner import RuntimeRunner


class OversizedTokenEstimator:
    def estimate_payload(self, payload: dict) -> dict:
        return {
            "estimated_tokens": 5001,
            "method": "test",
            "warning": True,
        }


class RecordingAdapter:
    def __init__(self):
        self.last_payload = None

    def invoke(self, runtime_payload: dict) -> dict:
        self.last_payload = runtime_payload

        return {
            "adapter": {
                "name": "recording",
                "version": "0.1.0",
            },
            "execution": {
                "success": True,
                "execution_time_ms": 0,
                "token_estimate": 0,
            },
            "output": {
                "implementation_summary": (
                    "Recording adapter executed."
                ),
                "validation_summary": (
                    "Validation passed."
                ),
                "confidence_gate": "Confidence: 90%",
                "known_gaps": [],
                "handoff": "Ready for review.",
            },
            "governance": {
                "confidence_score": 90,
                "human_validation_required": False,
            },
            "errors": [],
        }



def test_runner_emits_token_warning():
    runner = RuntimeRunner()

    runner.token_estimator = (
        OversizedTokenEstimator()
    )

    result = runner.run(
        "examples/runtime-task.yaml"
    )

    runtime_result = result["runtime_result"]

    assert runtime_result[
        "token_estimate"
    ]["warning"] is True

    assert (
        "token_warning" in runtime_result
    )



def test_runner_emits_telemetry_event():
    runner = RuntimeRunner()

    result = runner.run(
        "examples/runtime-task.yaml"
    )

    telemetry_event = result[
        "runtime_result"
    ]["telemetry_event"]

    assert telemetry_event["task_id"] == "STORY-001"

    assert telemetry_event[
        "execution_success"
    ] is True

    assert "estimated_tokens" in telemetry_event



def test_runner_uses_compiled_context_for_adapter_payload():
    runner = RuntimeRunner()

    recording_adapter = RecordingAdapter()

    runner.adapter_registry.get = (
        lambda adapter_name: recording_adapter
    )

    result = runner.run(
        "examples/runtime-task.yaml"
    )

    compiled_context = result[
        "runtime_result"
    ]["compiled_context"]

    adapter_payload = (
        recording_adapter.last_payload
    )

    assert (
        adapter_payload["runtime_context"]
        == compiled_context
    )

    assert "memory" in compiled_context

    assert compiled_context["memory"][0][
        "id"
    ] == "memory-001"
