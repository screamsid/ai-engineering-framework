# Worked Example: Python Automation Tool

This example shows how the AI Engineering Framework can be applied to a small Python automation project.

The example demonstrates:

- story intake
- risk classification
- runtime invocation
- builder output
- validation output
- reviewer output
- confidence gate
- formatter output
- memory candidate

## Scenario

Build a small Python CLI tool that reads a JSON inventory file and prints a summary of devices grouped by type.

This is intentionally simple.

The point is not the tool itself.

The point is to demonstrate framework flow.

## Example Files

```text
examples/python-automation/
├── README.md
├── PROJECT-PROFILE.md
├── WORKING-CONTEXT.md
├── STORY-001.md
├── RUNTIME-CALL.yaml
├── BUILDER-OUTPUT.md
├── REVIEWER-OUTPUT.md
├── FORMATTER-OUTPUT.md
├── MEMORY-CANDIDATE.md
└── AUDIT-LOG.md
```

## Risk Level

Risk: Low

Reason:

- local-only CLI tool
- no credentials
- no network access
- no production changes
- no destructive behaviour

## Expected Confidence Behaviour

Because this is low-risk work, autonomous execution is acceptable if confidence is at least 85% and validation evidence exists.
