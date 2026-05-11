from runtime.validators.basic_validator import RuntimeValidator


def test_validator_passes_valid_output():
    output = """
## Implementation Summary
Implemented feature.

## Validation Summary
Smoke tests passed.

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
    assert len(result["issues"]) > 0


def test_validator_detects_missing_risk():
    output = """
## Implementation Summary
Implemented feature.

## Validation Summary
Smoke tests passed.

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
        issue["message"] == "Risk classification missing"
        for issue in result["issues"]
    )
