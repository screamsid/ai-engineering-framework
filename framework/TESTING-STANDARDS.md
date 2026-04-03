---
name: testing-standards
description: Testing is mandatory for all meaningful changes.
---
# Testing Standards

Testing is mandatory for all meaningful changes.

The goal is not maximum ceremony.  
The goal is confidence proportional to risk.

---

## Core Rule

Every meaningful change must be validated.

At minimum:
- a smoke test is required

No change should be handed off as complete without validation.

---

## Levels of Testing

### 1. Smoke Testing (mandatory)

Required for all changes.

Examples:
- script runs successfully
- command completes without error
- expected output is produced
- endpoint responds correctly
- configuration loads without failure

---

### 2. Functional Testing

Required when logic changes.

Examples:
- functions return expected results
- parsing behaves correctly
- workflows produce expected outcomes

---

### 3. Integration Testing

Required when:

- multiple components interact
- external systems are involved
- APIs are used
- workflows span multiple steps

---

### 4. Security Validation

Required when the change affects:

- authentication or authorisation
- input handling
- secrets
- file handling
- subprocess execution
- dependencies
- APIs or external integrations
- sensitive data

---

## Builder Responsibilities

The Builder must clearly record:

- what was tested
- how it was tested
- what passed
- what failed (if anything)
- what was not tested
- why any gaps exist

---

## Reviewer Responsibilities

The Reviewer must confirm:

- testing is appropriate for the risk
- validation is clearly documented
- gaps are understood and acceptable

---

## Testing Gaps

Testing gaps are only acceptable if:

- explicitly stated
- understood
- low risk or temporary
- recorded clearly

Hidden gaps are not acceptable.

---

## Prohibited

Do not:

- claim completion without testing
- rely on assumptions instead of validation
- skip testing for “small” changes
- hide known issues
- treat manual guesswork as testing

---

## Proportional Testing

Not every change requires full test suites.

But every change requires enough validation to justify confidence.

---

## Output Expectations

Validation must be reported clearly:

- what was tested
- result
- any gaps
- any concerns

---

## Working Rule

If you cannot show how it was tested:

- it was not tested

---

## Enforcement

If validation is missing or unclear:

- the work is not complete
- the story must return for rework