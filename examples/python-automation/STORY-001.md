# STORY-001

## Objective

Create a Python CLI tool that:

- reads a JSON inventory file
- groups devices by type
- prints a readable summary

## In Scope

- JSON parsing
- grouping logic
- CLI execution
- readable output
- basic validation

## Out of Scope

- databases
- APIs
- authentication
- web frontend
- persistent storage

## Acceptance Criteria

- tool accepts JSON file path
- invalid JSON handled safely
- missing fields handled safely
- output grouped by device type
- tool exits cleanly on failure
- smoke test completed

## Initial Risk Classification

Low

## Initial Confidence

92%

Reason:

- simple local automation
- low blast radius
- no external integrations
- straightforward validation path
