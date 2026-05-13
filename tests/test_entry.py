from runtime.entry.runtime_call_builder import (
    RuntimeCallBuilder,
)
from runtime.version import get_framework_version


VALID_INPUT = {
    "task_id": "STORY-001",
    "task_type": "python-automation",
    "objective": (
        "Build a secure inventory summary CLI "
        "for infrastructure asset reporting."
    ),
    "scope": [
        "Build CLI entry point",
        "Add structured logging",
        "Add validation and smoke tests",
        "Generate human-readable output summary",
    ],
    "out_of_scope": [
        "Web UI",
        "Database persistence",
        "Multi-user authentication",
    ],
    "risk_level": "low",
    "confidence_score": 92,
    "validation_requirements": [
        "smoke-test",
        "validation-test",
        "logging-review",
    ],
    "stop_conditions": [
        "missing_acceptance_criteria",
        "validation_missing",
        "confidence_below_threshold",
        "unresolved_security_risk",
    ],
    "escalation_preferences": [
        "reviewer-check",
        "security-review",
    ],
    "success_criteria": [
        "CLI executes successfully",
        "Validation passes",
        "Confidence threshold remains above 85",
        "Structured logs are generated correctly",
    ],
    "created_by": "simon",
    "created_at": "2026-05-12T17:25:00Z",
    "notes": (
        "Safe local lifecycle validation "
        "using mock adapter only."
    ),
}


EXPECTED_RUNTIME_CALL = {
    "version": get_framework_version(),
    "task": {
        "id": "STORY-001",
        "type": "python-automation",
        "objective": (
            "Build a secure inventory summary CLI "
            "for infrastructure asset reporting."
        ),
        "scope": [
            "Build CLI entry point",
            "Add structured logging",
            "Add validation and smoke tests",
            "Generate human-readable output summary",
        ],
        "out_of_scope": [
            "Web UI",
            "Database persistence",
            "Multi-user authentication",
        ],
    },
    "governance": {
        "risk_level": "low",
        "confidence_score": 92,
        "confidence_threshold": 85,
        "mode": "standard",
        "preset": "python-automation",
    },
    "routing": {
        "preferred_role": "builder",
        "preferred_agent": "codex",
        "adapter": "mock",
    },
    "required_outputs": [
        "implementation_summary",
        "validation_summary",
        "confidence_gate",
        "known_gaps",
        "handoff",
    ],
    "stop_conditions": [
        "missing_acceptance_criteria",
        "validation_missing",
        "confidence_below_threshold",
        "unresolved_security_risk",
    ],
    "escalation": {
        "human_validation_required": False,
        "escalation_preferences": [
            "reviewer-check",
            "security-review",
        ],
    },
    "validation": {
        "required_tests": [
            "smoke-test",
            "validation-test",
            "logging-review",
        ],
        "success_criteria": [
            "CLI executes successfully",
            "Validation passes",
            "Confidence threshold remains above 85",
            "Structured logs are generated correctly",
        ],
    },
    "metadata": {
        "created_by": "simon",
        "created_at": "2026-05-12T17:25:00Z",
        "notes": (
            "Safe local lifecycle validation "
            "using mock adapter only."
        ),
    },
}



def test_runtime_call_builder_matches_worked_example():
    builder = RuntimeCallBuilder()

    runtime_call = builder.build(
        VALID_INPUT
    )

    assert runtime_call == EXPECTED_RUNTIME_CALL



def test_missing_required_field_raises_value_error():
    builder = RuntimeCallBuilder()

    invalid_input = VALID_INPUT.copy()

    del invalid_input["risk_level"]

    try:
        builder.build(invalid_input)
        assert False

    except ValueError as exc:
        assert (
            "Missing required field: risk_level"
            in str(exc)
        )



def test_invalid_risk_level_raises_value_error():
    builder = RuntimeCallBuilder()

    invalid_input = VALID_INPUT.copy()

    invalid_input["risk_level"] = "extreme"

    try:
        builder.build(invalid_input)
        assert False

    except ValueError as exc:
        assert "Invalid risk level" in str(exc)



def test_invalid_confidence_score_raises_value_error():
    builder = RuntimeCallBuilder()

    invalid_input = VALID_INPUT.copy()

    invalid_input["confidence_score"] = 101

    try:
        builder.build(invalid_input)
        assert False

    except ValueError as exc:
        assert (
            "Confidence score must be between 0 and 100"
            in str(exc)
        )
