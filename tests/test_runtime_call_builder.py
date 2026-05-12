from runtime.entry.runtime_call_builder import (
    RuntimeCallBuilder,
)


BASE_TASK_INPUT = {
    "task_id": "STORY-002",
    "task_type": "python-automation",
    "objective": "Validate runtime task input",
    "scope": ["validation"],
    "confidence_score": 90,
    "validation_requirements": ["smoke-test"],
    "stop_conditions": ["validation_failure"],
}


def test_validate_missing_risk_level_returns_single_error():
    builder = RuntimeCallBuilder()

    task_input = BASE_TASK_INPUT.copy()

    issues = builder.validate(task_input)

    assert issues.count(
        "Missing required field: risk_level"
    ) == 1

    assert "Invalid risk level" not in issues



def test_validate_invalid_risk_level_returns_single_error():
    builder = RuntimeCallBuilder()

    task_input = BASE_TASK_INPUT.copy()
    task_input["risk_level"] = "extreme"

    issues = builder.validate(task_input)

    assert issues.count(
        "Invalid risk level"
    ) == 1

    assert (
        "Missing required field: risk_level"
        not in issues
    )
