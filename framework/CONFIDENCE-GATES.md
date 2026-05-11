---
name: confidence-gates
description: Confidence-based decision gates for agent autonomy, human validation, and memory learning.
---
# Confidence Gates

Confidence gates turn framework guidance into enforceable decision points.

They define when an agent can proceed autonomously, when it must ask for human validation, and how the result becomes future learning.

## Core Principle

Agents may act autonomously only when confidence is high enough for the risk of the action.

If confidence is below the required threshold, the agent must pause and request human validation.

## Default Thresholds

| Confidence Score | Decision | Meaning |
| --- | --- | --- |
| 90-100% | Proceed autonomously | Strong evidence and low unresolved risk |
| 75-89% | Proceed only for low-risk work, otherwise ask human | Evidence exists but uncertainty remains |
| 50-74% | Human validation required | Too much uncertainty for autonomous action |
| 0-49% | Stop and escalate | Unsafe, unclear, or insufficiently validated |

## Risk Adjustment

Confidence thresholds must be adjusted by risk.

| Risk Level | Minimum Confidence To Proceed Without Human |
| --- | --- |
| Low | 85% |
| Medium | 90% |
| High | 95% |
| Critical | Human validation required regardless of score |

## Critical Actions Always Require Human Validation

Human validation is required for:

- destructive actions
- production changes
- credential or secret handling changes
- security control weakening
- data deletion
- major architecture changes
- external customer-impacting changes
- irreversible operations
- memory promotion with sensitive origin material

## Required Confidence Gate Format

Use this format before proceeding with meaningful action:

```markdown
## Confidence Gate

Action: <what the agent proposes to do>
Risk Level: Low / Medium / High / Critical
Confidence: High / Medium / Low
Score: 0-100%
Evidence: <why the score is justified>
Known Gaps: <uncertainties or missing validation>
Decision: Proceed / Ask Human / Stop / Escalate
Human Validation Required: Yes / No
```

## Human Validation Loop

When human validation is required:

1. pause before action
2. explain the decision point clearly
3. state the confidence score and reason
4. ask for approval, correction, or additional context
5. capture the human response
6. update project memory if the lesson is project-specific
7. propose framework memory only if the lesson is reusable and sanitised

## Learning From Human Validation

Human validation outcomes are valuable learning data.

After validation, the agent should identify:

- was the confidence score accurate?
- did the human approve, reject, or correct the action?
- what evidence was missing?
- what rule, skill, or memory would improve future confidence?
- should this become a candidate lesson?

## Candidate Learning Format

```markdown
## Confidence Learning Candidate

Original Action: <sanitised summary>
Original Confidence: <score and reason>
Human Decision: Approved / Rejected / Corrected / Deferred
What Changed: <sanitised summary>
Reusable Lesson: <abstracted lesson>
Recommended Destination: Project Memory / Framework Memory / Skill Pack / Roadmap / None
Confidence After Review: <score>
```

## Calibration Rule

Confidence must be calibrated over time.

If agents repeatedly rate actions above 90% and humans correct them, the framework must lower trust in similar future confidence claims.

If agents repeatedly request human approval for safe, repeatable actions, the framework should capture the pattern and allow future autonomous execution when evidence matches.

## Enforced Behaviour

The harness or reviewer should block completion when:

- confidence is missing
- confidence is below threshold and no human validation occurred
- risk level is not stated
- known gaps are hidden
- critical actions proceeded without approval

## Non-Hindrance Rule

Confidence gates must not become unnecessary friction.

For low-risk, repeatable, well-validated actions, agents should proceed when confidence is high enough.

The goal is not to ask humans everything.

The goal is to ask humans at the right moments, learn from the answer, and reduce repeat uncertainty safely.

## Completion Rule

Confidence gates are successful when they reduce unsafe autonomy without turning every action into a manual approval process.
