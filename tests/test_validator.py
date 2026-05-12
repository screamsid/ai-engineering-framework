from pathlib import Path

from runtime.validators.basic_validator import RuntimeValidator


def test_validator_passes_valid_output():
    output = """
## Implementation Summary
Implemented feature.

## Validation Summary
Smoke validation checks passed.

## Confidence Gate
Confidence: 92%
Risk Level: Low

## Known Gaps
No live testing.

## Handoff
Ready for review.
"""

    validator = RuntimeValidator()
    result = validator.validate(output)

    assert result["passed"] is True


def test_validator_detects_missing_sections():
    output = """
## Implementation Summary
Implemented feature.

## Confidence Gate
Confidence: 92%
Risk Level: Low
"""

    validator = RuntimeValidator()
    result = validator.validate(output)

    assert result["passed"] is False
    assert any(
        issue["section"] == "validation_summary"
        for issue in result["issues"]
    )


def test_validator_detects_missing_risk():
    output = """
## Implementation Summary
Implemented feature.

## Validation Summary
Smoke validation checks passed.

## Confidence Gate
Confidence: 92%

## Known Gaps
No live testing.

## Handoff
Ready for review.
"""

    validator = RuntimeValidator()
    result = validator.validate(output)

    assert any(
        issue["section"] == "confidence_gate"
        and issue["field"] == "pattern_validation"
        for issue in result["issues"]
    )


def test_valid_example_output_passes():
    output = Path(
        "runtime/output/examples/valid-output.md"
    ).read_text(encoding="utf-8")

    validator = RuntimeValidator()
    result = validator.validate(output)

    assert result["passed"] is True
    assert result["issue_count"] == 0


def test_invalid_example_output_fails_with_structured_errors():
    output = Path(
        "runtime/output/examples/invalid-output.md"
    ).read_text(encoding="utf-8")

    validator = RuntimeValidator()
    result = validator.validate(output)

    assert result["passed"] is False
    assert result["issue_count"] > 0
    assert all(
        "section" in issue
        and "field" in issue
        and "message" in issue
        for issue in result["issues"]
    )
