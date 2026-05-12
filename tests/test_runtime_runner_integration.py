from runtime.runner import RuntimeRunner


class OversizedTokenEstimator:
    def estimate_payload(self, payload: dict) -> dict:
        return {
            "estimated_tokens": 5001,
            "method": "test",
            "warning": True,
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

    result = runner.run(
        "examples/runtime-task.yaml"
    )

    compiled_context = result[
        "runtime_result"
    ]["compiled_context"]

    adapter_context = result[
        "runtime_result"
    ]["adapter_result"]

    assert "memory" in compiled_context

    assert compiled_context["task"] == {
        "id": "STORY-001",
        "type": "python-automation",
        "objective": "Build inventory summary CLI",
        "scope": [
            "Build CLI entry point",
            "Add smoke tests",
        ],
        "out_of_scope": [
            "Web UI",
        ],
    }
