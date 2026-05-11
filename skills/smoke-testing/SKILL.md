# Smoke Testing Skill

## Purpose

Provide fast, lightweight validation that confirms core functionality works after a change.

Smoke testing exists to detect obvious breakage quickly before deeper validation.

## Core Checks

- application starts
- command executes successfully
- endpoint responds
- configuration loads
- authentication flow responds
- expected output appears
- no immediate runtime failure occurs

## Required Outputs

- smoke_test_summary
- validation_summary
- confidence_gate
- known_gaps

## Required Validation

- verify command or service execution
- verify expected response exists
- verify no obvious runtime failure

## Stop Conditions

- service fails to start
- command crashes
- endpoint unreachable
- configuration invalid
- authentication failure

## Confidence Guidance

Lower confidence when:

- smoke testing was partial
- environment differs from target
- dependencies were unavailable
- execution was simulated rather than run

## Candidate Lessons

This skill should propose memory candidates when:

- repeated startup failures occur
- deployment regressions repeat
- a useful validation shortcut is identified
- a recurring smoke-test anti-pattern is found
