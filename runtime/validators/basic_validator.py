"""
Structured runtime validator.

Purpose:
- validate required sections
- validate required fields within sections
- produce structured validation errors
- support canonical output contract enforcement

This validator intentionally focuses on:
- operational safety
- required outputs
- uncertainty visibility
- governance completeness

It does NOT enforce:
- writing style
- cosmetic formatting
- presentation preferences
"""

from dataclasses import dataclass
import re
from typing import List


@dataclass
class ValidationIssue:
    severity: str
    section: str
    field: str
    message: str


REQUIRED_STRUCTURE = {
    "implementation_summary": {
        "required_patterns": [
            r"implemented|updated|created|validated",
        ],
    },
    "validation_summary": {
        "required_patterns": [
            r"test|validation|review|check",
        ],
    },
    "confidence_gate": {
        "required_patterns": [
            r"confidence\s*:\s*(\d+%)",
            r"risk\s*(level)?\s*:\s*(low|medium|high|critical)",
        ],
    },
    "known_gaps": {
        "required_patterns": [],
    },
    "handoff": {
        "required_patterns": [
            r"ready|review|handoff|next",
        ],
    },
}


SECTION_PATTERN = re.compile(
    r"^##\s+([a-zA-Z0-9_\- ]+)",
    re.MULTILINE,
)


class RuntimeValidator:
    """Structured operational validator."""

    def extract_sections(self, text: str) -> dict:
        matches = list(SECTION_PATTERN.finditer(text))
        sections = {}

        for index, match in enumerate(matches):
            section_name = (
                match.group(1)
                .strip()
                .lower()
                .replace(" ", "_")
            )

            start = match.end()

            if index + 1 < len(matches):
                end = matches[index + 1].start()
            else:
                end = len(text)

            sections[section_name] = text[start:end].strip()

        return sections

    def validate(self, output_text: str) -> dict:
        issues: List[ValidationIssue] = []

        sections = self.extract_sections(output_text)

        for section_name, rules in REQUIRED_STRUCTURE.items():
            section_content = sections.get(section_name)

            if not section_content:
                issues.append(
                    ValidationIssue(
                        severity="high",
                        section=section_name,
                        field="section",
                        message=f"Missing required section: {section_name}",
                    )
                )
                continue

            for pattern in rules["required_patterns"]:
                if not re.search(
                    pattern,
                    section_content,
                    re.IGNORECASE,
                ):
                    issues.append(
                        ValidationIssue(
                            severity="medium",
                            section=section_name,
                            field="pattern_validation",
                            message=(
                                f"Section '{section_name}' failed required validation pattern: {pattern}"
                            ),
                        )
                    )

        passed = not any(
            issue.severity == "high"
            for issue in issues
        )

        return {
            "passed": passed,
            "issue_count": len(issues),
            "issues": [
                {
                    "severity": issue.severity,
                    "section": issue.section,
                    "field": issue.field,
                    "message": issue.message,
                }
                for issue in issues
            ],
            "detected_sections": list(sections.keys()),
        }


if __name__ == "__main__":
    VALID_OUTPUT = """
## Implementation Summary
Implemented structured output validation improvements.

## Validation Summary
Validation tests and runtime review completed.

## Confidence Gate
Confidence: 92%
Risk Level: Medium

## Known Gaps
- No live external adapter execution yet.

## Handoff
Ready for reviewer validation.
"""

    INVALID_OUTPUT = """
## Implementation Summary
Stuff changed.

## Confidence Gate
Confidence: maybe okay.
"""

    validator = RuntimeValidator()

    print("VALID OUTPUT RESULT")
    print(validator.validate(VALID_OUTPUT))

    print("INVALID OUTPUT RESULT")
    print(validator.validate(INVALID_OUTPUT))
