---
name: confidence-calibration
description: Standards for calibrating agent confidence against real-world outcomes and human validation.
---
# Confidence Calibration

Confidence is useful only if it reflects reality.

Agents must improve confidence accuracy over time by comparing predictions against actual outcomes.

## Core Principle

Confidence is not a feeling.

Confidence is an evidence-based estimate that should become more accurate through feedback and validation.

## Calibration Loop

1. agent proposes action
2. confidence score is assigned
3. action proceeds or requests human validation
4. outcome is observed
5. outcome is compared against original confidence
6. calibration data is recorded
7. future confidence scoring improves

## Calibration Signals

Useful calibration signals include:

- human approval rate
- human correction rate
- rollback frequency
- validation failures
- post-release defects
- security findings
- reviewer disagreement
- false positives
- false negatives
- production incidents

## Overconfidence Detection

The framework should detect when:

- agents repeatedly rate weak conclusions too highly
- validation gaps are ignored
- reviewers frequently reject high-confidence outputs
- risky actions are underestimated

Repeated overconfidence should reduce future trust weighting.

## Underconfidence Detection

The framework should detect when:

- agents repeatedly escalate safe work unnecessarily
- low-risk work is blocked too often
- humans consistently approve low-confidence actions
- the framework introduces unnecessary friction

Repeated underconfidence should increase future autonomy where safe.

## Calibration Metadata

Calibration records should include:

```markdown
### Calibration Record
Action Type: <task type>
Original Confidence: <score>
Risk Level: <risk>
Human Validation: Approved / Rejected / Corrected
Validation Outcome: Passed / Failed / Partial
Post-Outcome Result: Success / Incident / Rollback / Rework
Calibration Impact: Increase Trust / Reduce Trust / No Change
```

## Confidence Weighting

Confidence should eventually become weighted by:

- historical accuracy
- task domain
- validation quality
- reviewer agreement
- memory reliability
- skill maturity

## Completion Rule

A confidence system is healthy when:

- confidence becomes more accurate over time
- unnecessary escalations decrease
- unsafe autonomy decreases
- human trust improves
