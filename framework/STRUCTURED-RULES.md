---
name: structured-rules
description: Structured machine-readable role-card and rule standards for framework enforcement and automation.
---
# Structured Rules

Framework guidance should evolve from freeform text into structured machine-readable rules where enforcement adds operational value.

The canonical runtime structure is the `role_card` schema used in `runtime/rules/*.rule-card.yaml`.

Do not create competing schemas for the same enforcement purpose.

## Core Principle

Not every framework rule should be enforced.

Only high-value, measurable, low-friction controls should become structured enforcement rules.

Block on risk. Warn on style. Learn from everything.

## Canonical Runtime Object

The primary structured runtime object is a role card.

Role cards define:

- role purpose
- rules the role must follow
- required outputs
- required skills
- prohibited behaviours
- stop conditions
- confidence thresholds
- escalation requirements

## Role Card Format

```yaml
role_card:
  role: builder

  purpose:
    - implement approved work safely

  must_follow:
    - core-rules
    - confidence-gates
    - testing-standards

  required_outputs:
    - implementation_summary
    - validation_summary
    - confidence_gate
    - known_gaps
    - handoff

  required_skills:
    - secure-coding
    - smoke-testing

  must_not:
    - expand_scope
    - skip_validation
    - hide_uncertainty

  stop_conditions:
    - missing_acceptance_criteria
    - unresolved_security_risk
    - confidence_below_threshold

  confidence:
    minimum_autonomous_score:
      low: 85
      medium: 90
      high: 95

  escalation:
    require_human_validation_below_threshold: true
```

## Rule Categories

| Category | Purpose |
| --- | --- |
| Required Outputs | Ensure mandatory sections exist |
| Confidence Rules | Control autonomy and escalation |
| Validation Rules | Ensure proportional testing |
| Security Rules | Enforce security review requirements |
| Adherence Rules | Detect framework drift |
| Memory Rules | Control memory promotion |
| Risk Rules | Adjust validation and autonomy |
| Formatter Rules | Preserve meaning between machine and human versions |

## Severity Levels

| Severity | Meaning |
| --- | --- |
| Low | Log only or advisory warning |
| Medium | Correction recommended before handoff |
| High | Block autonomous completion |
| Critical | Block execution and require escalation |

## Enforcement Mapping

Structured enforcement should be derived from role cards.

Examples:

| Role Card Field | Runtime Use |
| --- | --- |
| required_outputs | Validate required markdown or structured sections |
| must_follow | Inject relevant framework guidance |
| required_skills | Load relevant skill packs |
| must_not | Check for prohibited behaviours during review |
| stop_conditions | Pause or escalate when triggered |
| confidence | Apply confidence thresholds |
| escalation | Require human validation where needed |

## Advisory Versus Enforced

Not all rules should block work.

| Rule Type | Enforcement |
| --- | --- |
| Formatting guidance | Advisory or Formatter role |
| Confidence missing | Enforced |
| Validation missing | Enforced |
| Minor wording issue | Advisory |
| High-risk work without security review | Enforced |
| Memory metadata missing | Usually advisory unless promoting framework memory |
| Style inconsistency | Warning only |

## Non-Hindrance Rule

Do not over-structure the framework.

The framework exists to improve operational quality, not create endless rigid workflow gates.

If enforcement creates more friction than value, reduce or simplify the rule.

## Recommended Initial Enforcement

Start with:

- confidence gate required
- risk classification required
- validation summary required
- known gaps required
- handoff required
- human validation below threshold
- security review for high-risk work

## Completion Rule

Structured rules are successful when they reduce unsafe behaviour and hidden uncertainty while keeping agents operationally effective.
