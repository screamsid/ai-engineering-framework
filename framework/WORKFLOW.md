---
name: workflow
description: Standard delivery workflow with confidence gates, risk classification, validation, review, formatting, and escalation.
---
# Workflow

This defines the standard delivery flow for all work using this framework.

The goal is to:

- make execution predictable
- reduce ambiguity
- improve handoffs
- support review and rollback
- stop work drifting out of control
- make confidence and risk visible
- escalate only where risk justifies it
- separate machine-valid output from human-readable presentation

## Standard Story Flow

1. Story intake
2. Story review
3. Clarification, risk identification, and confidence preflight
4. Planning
5. Implementation
6. Validation and confidence gate
7. Review
8. Security review when required
9. Git checks
10. Release check
11. Optional formatting for human-readable handoff
12. Completion, memory review, or rework

---

## 1. Story Intake

A story must define:

- objective
- scope
- out of scope
- acceptance criteria
- constraints if known

If this is missing, the story is not ready.

---

## 2. Story Review: Planner

The Planner must:

- confirm objective is clear
- confirm scope boundaries
- identify missing detail
- identify dependencies
- identify risks
- confirm acceptance criteria
- assign an initial risk classification

### Output

- understanding
- gaps
- risks
- initial risk classification
- readiness assessment

If the story is unclear:

- do not proceed blindly

---

## 3. Clarification, Risk Identification, and Confidence Preflight

Before planning:

- surface ambiguity
- identify assumptions
- identify technical risks
- identify security concerns
- identify validation needs
- identify rollback considerations
- assign or confirm risk level using `RISK-CLASSIFICATION.md`
- identify whether human validation is likely to be required

### Rule

Unclear work must be made explicit before execution.

If confidence is already below the required threshold for the risk level, human validation is required before proceeding.

---

## 4. Planning: Planner

The Planner produces:

- step-by-step plan
- areas/files likely impacted
- validation approach
- confidence gate expectations
- rollback considerations
- backlog items that are out of scope

### Requirements

- steps must be small
- plan must be actionable
- plan must not assume hidden context
- confidence thresholds must match risk level

---

## 5. Implementation: Builder

The Builder:

- follows the plan
- works in small steps
- keeps scope tight
- reuses existing code where possible
- updates docs if needed
- updates audit log
- records backlog items

### Rules

- no scope creep
- no large mixed changes
- no skipping validation
- no confidence inflation to avoid human validation

---

## 6. Validation and Confidence Gate: Builder

Before handoff, Builder must:

- run smoke tests at minimum
- run deeper tests where risk requires it
- record what was tested
- record what was not tested
- state results clearly
- include a confidence gate using `CONFIDENCE-GATES.md`
- state known gaps
- state whether human validation is required

### Output

- validation summary
- known gaps
- confidence gate
- human validation requirement

If confidence is below the required threshold:

- stop
- ask for human validation
- record the outcome for calibration

---

## 7. Review: Reviewer

Reviewer checks:

- does it meet the story objective
- are acceptance criteria met
- is scope respected
- is it maintainable
- is validation sufficient for the risk level
- are confidence and known gaps stated
- are docs updated
- is audit log updated
- did the agent follow the framework

### Output

- pass or changes required
- findings
- risks
- adherence assessment
- confidence gate

Review should block on risk and warn on style.

---

## 8. Security Review: When Required

Security review is required when risk classification, scope, or implementation affects:

- auth or permissions
- secrets
- external inputs
- file handling
- subprocess execution
- dependencies
- APIs
- sensitive data
- production security controls
- user or customer data

Security Reviewer checks:

- attack surface
- input handling
- secret handling
- dependency risk
- logging safety
- trust boundaries
- abuse paths

### Output

- pass / concerns / fail
- required fixes
- security findings
- risk assessment
- confidence gate

High and critical risk work must follow `RISK-CLASSIFICATION.md` and `CONFIDENCE-GATES.md`.

---

## 9. Git Checks: Git Manager

Check:

- branch naming
- commit structure
- commit messages
- change grouping
- rollback feasibility

### Output

- pass or changes required
- rollback assessment

---

## 10. Release Check: Release Manager

Confirm:

- definition of done met
- reviews complete
- validation complete
- confidence gate present
- human validation completed where required
- audit log updated
- backlog items captured
- tagging requirements met
- rollback path understood

### Output

- ready or not ready
- summary
- outstanding items
- confidence gate
- release decision

---

## 11. Optional Formatting: Formatter

The Formatter may be used after validation, review, security review, or release check when a human-readable version is needed.

The Formatter must:

- preserve meaning
- preserve confidence scores
- preserve risk levels
- preserve findings
- preserve known gaps
- preserve escalation requirements
- avoid interpretation
- avoid spin

The Formatter must not:

- change decisions
- soften risk
- hide uncertainty
- add missing information
- turn incomplete work into complete work

Formatting is presentation only.

Machine-readable output remains the canonical source of truth.

---

## 12. Completion, Memory Review, or Rework

A story is complete only when:

- all checks pass
- definition of done is satisfied
- handoff is clear
- confidence and risk are documented
- human validation has occurred where required

If useful lessons were identified:

- propose a memory candidate
- route it to the Memory Reviewer
- sanitise before framework memory promotion

---

## Loopback Rule

If any stage fails:

- work returns to the correct role
- findings must be explicit
- rework must be targeted
- confidence and risk must be reassessed

Failure is part of the process, not a breakdown of it.

---

## Handoff Rules

Every handoff must include:

- current state
- what changed
- validation status
- confidence gate
- known risks
- known gaps
- next step

No implicit knowledge transfer.

If a human-readable handoff is generated, the Formatter may be used only after canonical machine-readable content is complete.

---

## Execution Principles

- plan first, then act
- make uncertainty visible
- classify risk early
- use confidence to control autonomy
- keep changes small
- protect scope
- record decisions
- surface risk early
- maintain working context
- preserve machine-readable truth
- use formatting only for presentation
- block on risk
- warn on style
- learn from everything

---

## Workflow Integrity

This workflow must be followed.

If steps are skipped:

- quality drops
- risk increases
- traceability is lost
- rework increases
- calibration quality suffers

Consistency is the goal.
