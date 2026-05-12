# Invocation Contract Guide

## Purpose

The invocation contract is the canonical input specification for framework tasks.

This is the top-level human-to-runtime handoff.

A human fills in the invocation contract to describe:

- what should be done
- how risky it is
- what outputs are required
- when execution should stop or escalate
- what level of confidence is acceptable

The runtime then uses this information for:

- routing
- context compilation
- adapter selection
- validation
- calibration
- governance decisions

---

# Structure Overview

```yaml
version:
task:
governance:
routing:
required_outputs:
stop_conditions:
escalation:
validation:
metadata:
```

---

# Field Reference

## version

Framework contract version.

Example:

```yaml
version: "0.3.1"
```

This allows the runtime to evolve safely over time.

---

# task

Describes the work itself.

## task.id

Stable task identifier.

Example:

```yaml
id: STORY-001
```

## task.type

Used for routing and preset selection.

Examples:

- python-automation
- infra-automation
- framework-design
- security-tool

## task.objective

Plain-English description of the intended outcome.

Good:

```yaml
objective: Build a secure inventory summary CLI.
```

Bad:

```yaml
objective: Fix stuff.
```

## task.scope

Work explicitly included.

## task.out_of_scope

Work explicitly excluded.

This prevents uncontrolled expansion.

---

# governance

Defines runtime governance expectations.

## governance.risk_level

Allowed values:

- low
- medium
- high
- critical

Critical risk always requires human validation.

## governance.confidence_score

Starting confidence estimate for autonomous execution.

Range:

```text
0-100
```

## governance.confidence_threshold

Minimum score required for autonomous execution.

If runtime confidence falls below this threshold:

- execution pauses
- escalation may occur

## governance.mode

Controls runtime depth.

Modes:

- lightweight
- standard
- full

## governance.preset

Loads expected behaviour and governance defaults.

Example:

```yaml
preset: python-automation
```

---

# routing

Optional execution preferences.

## preferred_role

Preferred role if already known.

## preferred_agent

Preferred execution adapter.

Examples:

- mock
- codex
- claude-code
- antigravity

## adapter

Explicit runtime adapter selection.

Use:

```yaml
adapter: mock
```

for safe lifecycle testing.

---

# required_outputs

Sections that must exist before completion.

Recommended defaults:

- implementation_summary
- validation_summary
- confidence_gate
- known_gaps
- handoff

---

# stop_conditions

Defines when execution must stop or escalate.

Recommended:

```yaml
- confidence_below_threshold
```

This prevents unsafe autonomy.

---

# escalation

Defines human escalation requirements.

## human_validation_required

Boolean.

Critical-risk tasks should always set this to true.

## escalation_preferences

Preferred escalation types.

Examples:

- reviewer-check
- security-review
- release-manager

---

# validation

Defines required testing and success conditions.

## required_tests

Examples:

- smoke-test
- validation-test
- security-review

## success_criteria

Defines what "done" means.

These should align to story acceptance criteria.

---

# metadata

Optional traceability information.

## created_by

Who created the invocation.

## created_at

Timestamp for auditing.

## notes

Additional human context.

Do not include secrets.

---

# Core Principle

The invocation contract exists to make:

- execution explicit
- governance inspectable
- autonomy bounded
- routing deterministic
- escalation predictable

The runtime should never rely on hidden assumptions.
