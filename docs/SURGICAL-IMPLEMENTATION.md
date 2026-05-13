# Surgical Implementation Pattern

Most real engineering work is not greenfield development.

Most real engineering work is:

- fixing bugs
- modifying existing behaviour
- extending APIs carefully
- refactoring small sections safely
- reducing blast radius
- preserving operational stability

The AI Engineering Framework already supports this operating model naturally.

This document names that pattern explicitly.

The framework calls this:

> Surgical Implementation

The goal is not maximum autonomy.

The goal is:

- bounded change
- explicit scope
- calibrated confidence
- visible unknowns
- human-reviewed diffs
- validation before merge

---

# Core Principle

The framework treats existing systems as operational environments, not blank canvases.

That means:

- read before write
- constrain scope before execution
- validate before merge
- declare uncertainty explicitly
- optimise for safety and maintainability over generation volume

---

# The Six-Step Pattern

## 1. Read First, Write Never Without Scope

The framework defines the surgical boundary before any modification occurs.

This is enforced through:

- `task.scope`
- `task.out_of_scope`
- runtime invocation payloads
- adapter governance constraints

Example:

```yaml
scope:
  - Fix token estimation overflow in token_estimator.py
  - Add validation test coverage

out_of_scope:
  - Runtime router changes
  - Telemetry schema redesign
  - Cost tracking implementation
```

This creates:

- explicit blast-radius boundaries
- reviewer-visible intent
- safer execution behaviour
- cleaner handoffs

The adapter receives these constraints directly.

The framework assumes:

> anything outside scope should remain untouched unless escalated explicitly.

---

## 2. Confidence Is Set Against What You Know

The framework does not treat confidence as optimism.

Confidence represents:

- familiarity with the codebase
- understanding of dependencies
- certainty about downstream effects
- validation completeness

This is enforced through:

- `confidence_score`
- confidence thresholds
- calibration feedback
- governance escalation

Example:

| Situation | Suggested Confidence |
| --- | --- |
| Small isolated bug in familiar module | 90-95 |
| Refactor in partially known subsystem | 70-85 |
| Legacy code with unknown dependencies | 40-65 |

Lower confidence naturally produces:

- tighter governance
- more reviewer involvement
- more conservative execution
- stronger escalation pressure

The framework intentionally rewards honesty over false certainty.

---

## 3. Token Estimation Gates Context Size

Surgical implementation works best when context stays focused.

Loading an entire codebase into runtime context usually produces:

- unfocused output
- hallucinated dependencies
- excessive modification suggestions
- degraded reviewability

The framework already supports this through:

- `TokenEstimator`
- compiled runtime context
- scoped invocation payloads
- token threshold warnings

The pattern encourages:

- loading the relevant module only
- loading adjacent dependencies selectively
- minimising unrelated framework noise
- treating context size as operational risk

Good surgical work is usually narrow.

---

## 4. Known Gaps Are Mandatory

This is one of the most important framework behaviours.

The runtime output contract requires:

```text
## Known Gaps
```

This section forces the agent to declare:

- what could not be verified
- what was intentionally not modified
- uncertain downstream effects
- missing validation
- operational unknowns

For surgical implementation this becomes critical reviewer guidance.

Example:

```markdown
## Known Gaps
- Integration tests were not available for the telemetry pipeline
- No validation against real Codex CLI responses
- Cost calculations validated only against synthetic usage data
```

The goal is not perfect certainty.

The goal is visible uncertainty.

---

## 5. The Diff Is the Handoff

The framework treats the handoff as an operational artefact, not a formality.

The runtime output contract already includes:

```text
## Handoff
```

For surgical implementation this section should explain:

- what changed
- what intentionally did not change
- what reviewers should verify manually
- rollback considerations
- operational risks remaining

Example:

```markdown
## Handoff
Changed:
- Added token cost calculation fields to telemetry events
- Added estimation error tracking

Did not change:
- Runtime routing behaviour
- Confidence gate thresholds

Manual verification:
- Validate usage parsing against real Codex CLI responses
- Validate cost rates before production use

Rollback:
- Remove additive telemetry fields only
```

The handoff is effectively:

> the reviewer briefing.

---

## 6. Validation Before Merge, Not After

The framework already supports validation-first execution through:

- `stop_conditions`
- confidence gates
- runtime validation
- human validation requirements

The surgical pattern strengthens this further.

The surgical preset adds:

```yaml
- unreviewed_diff
```

as a default stop condition.

Meaning:

> no change should merge without a human reviewing the actual modification.

This is especially important for:

- refactors
- infrastructure automation
- security-sensitive changes
- existing production systems

---

# Worked Example

Scenario:

A developer needs to fix inaccurate token telemetry estimation in an existing runtime module.

Task:

```yaml
task:
  type: surgical-implementation
  objective: Improve token telemetry visibility without changing runtime execution behaviour

scope:
  - Add estimation error tracking
  - Add cost estimate telemetry fields
  - Update tests

out_of_scope:
  - Runtime governance redesign
  - Adapter execution changes
  - Billing infrastructure
```

Governance:

```yaml
governance:
  risk_level: medium
  confidence_score: 82
  confidence_threshold: 90
```

Runtime behaviour:

- router assigns conservative execution defaults
- reviewer involvement becomes mandatory
- suggest-mode execution is preferred
- token estimation warnings remain active
- validation must pass before completion

Expected output:

- narrow targeted changes
- explicit known gaps
- reviewer-oriented handoff
- minimal blast radius

---

# Surgical Implementation Preset

The framework includes a dedicated:

```text
surgical-implementation
```

preset.

Default behaviour includes:

- read-first discipline
- minimal blast radius
- mandatory diff review
- conservative approval mode
- reviewer-required routing
- explicit rollback expectations
- validation-first workflow

This preset intentionally biases toward:

- safe iteration
- maintainability
- operational trust

rather than maximum autonomy.

---

# Why This Matters

Greenfield generation is the easy case.

Real engineering work happens inside:

- legacy systems
- partially understood systems
- operationally sensitive systems
- shared ownership environments
- fragile dependency graphs

The framework already handles this well because it naturally enforces:

- scope boundaries
- confidence calibration
- explicit uncertainty
- reviewer visibility
- validation discipline

This document simply makes that operating model explicit.

---

# Final Principle

Surgical implementation is not:

- passive
- anti-autonomy
- slow for the sake of process

It is:

- bounded
- reviewable
- operationally aware
- confidence-calibrated
- designed to minimise unintended consequences

The goal is not:

> generate the most code.

The goal is:

> make the correct change with the smallest safe blast radius.
