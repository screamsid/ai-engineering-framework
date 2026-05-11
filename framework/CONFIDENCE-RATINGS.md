---
name: confidence-ratings
description: Standard confidence scoring for testing, reviews, security reviews, smoke tests, and handoffs.
---
# Confidence Ratings

Every meaningful validation, review, security review, smoke test, and release check must include a confidence rating.

The rating is not a vanity score.  
It is a short, explicit statement of how much trust the agent has in the result based on evidence.

## Required Format

Use this format in every validation or review output:

```markdown
### Confidence
Rating: High / Medium / Low
Score: 0-100%
Reason: <short evidence-based explanation>
Gaps: <known gaps, unknowns, or not-tested areas>
Next action: <approve / rework / test deeper / escalate>
```

## Rating Scale

### High confidence: 80-100%
Use only when:

- the relevant tests or checks were run
- the results passed
- the change is well understood
- risk is low or mitigated
- gaps are minor and explicitly documented

High confidence does not mean risk-free.  
It means the conclusion is well supported by evidence.

### Medium confidence: 50-79%
Use when:

- some validation was completed
- evidence supports the conclusion
- there are known gaps
- impact is limited or acceptable
- more testing would improve certainty

Medium confidence is acceptable for lower-risk work if gaps are documented.

### Low confidence: 0-49%
Use when:

- testing was not run
- results are missing or inconclusive
- the agent is relying on inspection only
- risk is high or poorly understood
- required checks could not be completed

Low confidence must not be presented as complete.  
The next action must be rework, deeper testing, or escalation.

## Evidence Rules

Confidence must be based on evidence, not vibes.

Good evidence includes:

- command output
- passing tests
- reproduced behaviour
- reviewed diff
- dependency scan result
- static analysis result
- successful smoke test
- documented manual check

Weak evidence includes:

- “looks fine”
- “should work”
- assumptions about external systems
- unverified reasoning
- tests that were planned but not run

## Mandatory Use Cases

Confidence ratings are mandatory for:

- smoke tests
- functional tests
- integration tests
- security validation
- code review
- security review
- git/release readiness checks
- incident or defect analysis
- architecture review
- handoff summaries

## Completion Rule

A story cannot be marked complete unless the final handoff includes a confidence rating.

If confidence is below 80%, the handoff must explain whether the remaining risk is accepted or whether more work is required.

## Agent Instruction

Agents must not hide uncertainty.  
If unsure, state it clearly, assign a lower confidence rating, explain why, and recommend the next safest action.
