"""
Basic runtime validator prototype.

Purpose:
- validate required markdown sections
- validate confidence gate structure
- validate risk classification presence
- provide lightweight operational enforcement

This validator intentionally focuses on:
- operational safety
- required outputs
- uncertainty visibility

It does NOT enforce:
- writing style
- formatting perfection
- cosmetic structure
"""

from dataclasses import dataclass
import re
from typing import List


@dataclass
class ValidationIssue:
    severity: str
    message: str


REQUIRED_SECTIONS = [
    "implementation_summary",
    "validation_summary",
    "confidence_gate",
    "known_gaps",
    "handoff",
]


SECTION_PATTERN = re.compile(
    r"^##\s+([a-zA-Z0-9_\- ]+)",
    re.MULTILINE,
)


CONFIDENCE_PATTERN = re.compile(
    r"confidence\s*:\s*(high|medium|low|\d+%)",
    re.IGNORECASE,
)


RISK_PATTERN = re.compile(
    r"risk\s*(level)?\s*:\s*(low|medium|high|critical)",
    re.IGNORECASE,
)


class RuntimeValidator:
    """
    Lightweight operational validator.

    Focuses on:
    - required sections
    - risk visibility
    - confidence visibility
    - operational completeness
    """

    def extract_sections(self, text: str) -> List[str]:
        matches = SECTION_PATTERN.findall(text)

        return [
            match.strip().lower().replace(" ", "_")
            for match in matches
        ]

    def validate(self, output_text: str) -> dict:
        issues = []

        discovered_sections = self.extract_sections(output_text)

        for required_section in REQUIRED_SECTIONS:
            if required_section not in discovered_sections:
                issues.append(
                    ValidationIssue(
                        severity="high",
                        message=f"Missing required section: {required_section}",
                    )
                )

        if not CONFIDENCE_PATTERN.search(output_text):
            issues.append(
                ValidationIssue(
                    severity="medium",
                    message="Confidence information missing",
                )
            )

        if not RISK_PATTERN.search(output_text):
            issues.append(
                ValidationIssue(
                    severity="medium",
                    message="Risk classification missing",
                )
            )

        passed = not any(
            issue.severity == "high"
            for issue in issues
        )

        return {
            "passed": passed,
            "issues": [
                {
                    "severity": issue.severity,
                    "message": issue.message,
                }
                for issue in issues
            ],
            "detected_sections": discovered_sections,
        }


if __name__ == "__main__":
    SAMPLE_OUTPUT = """
## Implementation Summary
Implemented structured validation improvements.

## Validation Summary
Smoke testing completed successfully.

## Confidence Gate
Confidence: 92%
Risk Level: Medium
Decision: Proceed

## Known Gaps
No live integration testing performed.

## Handoff
Ready for reviewer validation.
"""

    validator = RuntimeValidator()
    result = validator.validate(SAMPLE_OUTPUT)

    print(result)
