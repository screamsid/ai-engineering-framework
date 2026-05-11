"""
Basic runtime validator prototype.

Purpose:
- validate required output sections
- validate confidence gate presence
- validate required risk level
- prepare for future harness integration

This is intentionally lightweight.
The goal is early operational enforcement without excessive rigidity.
"""

REQUIRED_SECTIONS = [
    "implementation_summary",
    "validation_summary",
    "confidence_gate",
    "known_gaps",
    "handoff",
]


def validate_output(output_text: str) -> dict:
    """
    Validate required framework sections.
    """

    results = {
        "passed": True,
        "missing_sections": [],
        "warnings": [],
    }

    lower_output = output_text.lower()

    for section in REQUIRED_SECTIONS:
        if section not in lower_output:
            results["missing_sections"].append(section)

    if results["missing_sections"]:
        results["passed"] = False

    if "confidence" not in lower_output:
        results["warnings"].append(
            "Confidence information missing"
        )

    if "risk" not in lower_output:
        results["warnings"].append(
            "Risk classification missing"
        )

    return results


if __name__ == "__main__":
    sample_output = """
    implementation_summary
    validation_summary
    confidence_gate
    known_gaps
    handoff
    """

    result = validate_output(sample_output)
    print(result)
