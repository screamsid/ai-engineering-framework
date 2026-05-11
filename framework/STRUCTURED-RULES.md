---
name: structured-rules
description: Structured machine-readable rule standards for framework enforcement and automation.
---
# Structured Rules

Framework guidance should evolve from freeform text into structured machine-readable rules where enforcement adds operational value.

## Core Principle

Not every framework rule should be enforced.

Only high-value, measurable, low-friction controls should become structured enforcement rules.

## Structured Rule Goals

Structured rules should:

- reduce agent drift
- improve adherence
- improve validation quality
- improve confidence handling
- reduce hidden uncertainty
- support automation
- support harness integration

## Structured Rule Format

Example:

```yaml
rule:
  id: confidence-required
  applies_to:
    - builder
    - reviewer
    - security-reviewer

  severity: high

  required_outputs:
    - confidence_gate

  fail_if_missing: true

  escalation:
    below_threshold: require_human_validation
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

## Severity Levels

| Severity | Meaning |
| --- | --- |
| Low | Warning only |
| Medium | Correction required before handoff |
| High | Block autonomous completion |
| Critical | Block execution and require escalation |

## Example Rules

### Confidence Gate Rule

```yaml
rule:
  id: confidence-gate-required
  applies_to:
    - builder
    - reviewer

  severity: high

  required_outputs:
    - confidence_gate

  fail_if_missing: true
```

### Human Validation Rule

```yaml
rule:
  id: low-confidence-human-validation

  condition:
    confidence_below: 90
    risk_level:
      - medium
      - high
      - critical

  action:
    require_human_validation: true
```

### Security Review Rule

```yaml
rule:
  id: security-review-required

  applies_to:
    - builder

  condition:
    risk_level:
      - high
      - critical

  action:
    require_role:
      - security-reviewer
```

## Advisory Versus Enforced

Not all rules should block work.

| Rule Type | Enforcement |
| --- | --- |
| Formatting guidance | Advisory |
| Confidence missing | Enforced |
| Validation missing | Enforced |
| Minor wording issue | Advisory |
| High-risk work without security review | Enforced |
| Memory metadata missing | Usually advisory |

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
