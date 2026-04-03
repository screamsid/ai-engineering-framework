---
name: workflow
description: 1. Story intake
---
# Workflow
This defines the standard delivery flow for all work using this framework.

The goal is to:
- make execution predictable
- reduce ambiguity
- improve handoffs
- support review and rollback
- stop work drifting out of control

## Standard story flow

1. Story intake
2. Story review
3. Clarification and risk identification
4. Planning
5. Implementation
6. Validation
7. Review
8. Security review (when required)
9. Git checks
10. Release check
11. Completion or rework

---

## 1. Story Intake

A story must define:

- objective
- scope
- out of scope
- acceptance criteria
- constraints (if known)

If this is missing, the story is not ready.

---

## 2. Story Review (Planner)

The Planner must:

- confirm objective is clear
- confirm scope boundaries
- identify missing detail
- identify dependencies
- identify risks
- confirm acceptance criteria

### Output:
- understanding
- gaps
- risks
- readiness assessment

If the story is unclear:
- do not proceed blindly

---

## 3. Clarification and Risk Identification

Before planning:

- surface ambiguity
- identify assumptions
- identify technical risks
- identify security concerns
- identify validation needs
- identify rollback considerations

### Rule:
Unclear work must be made explicit before execution.

---

## 4. Planning (Planner)

The Planner produces:

- step-by-step plan
- areas/files likely impacted
- validation approach
- rollback considerations
- backlog items (out of scope)

### Requirements:
- steps must be small
- plan must be actionable
- plan must not assume hidden context

---

## 5. Implementation (Builder)

The Builder:

- follows the plan
- works in small steps
- keeps scope tight
- reuses existing code where possible
- updates docs if needed
- updates audit log
- records backlog items

### Rules:
- no scope creep
- no large mixed changes
- no skipping validation

---

## 6. Validation (Builder)

Before handoff, Builder must:

- run smoke tests (minimum)
- run deeper tests where needed
- record what was tested
- record what was not tested
- state results clearly

### Output:
- validation summary
- gaps (if any)

---

## 7. Review (Reviewer)

Reviewer checks:

- does it meet the story objective
- are acceptance criteria met
- is scope respected
- is it maintainable
- is validation sufficient
- are docs updated
- is audit log updated

### Output:
- pass or changes required
- findings
- risks

---

## 8. Security Review (if required)

Required when work affects:

- auth or permissions
- secrets
- external inputs
- file handling
- subprocess execution
- dependencies
- APIs
- sensitive data

Security Reviewer checks:

- attack surface
- input handling
- secret handling
- dependency risk
- logging safety

### Output:
- pass / concerns / fail
- required fixes

---

## 9. Git Checks (Git Manager)

Check:

- branch naming
- commit structure
- commit messages
- change grouping
- rollback feasibility

### Output:
- pass or changes required

---

## 10. Release Check (Release Manager)

Confirm:

- definition of done met
- reviews complete
- validation complete
- audit log updated
- backlog items captured
- tagging requirements met

### Output:
- ready or not ready
- summary
- outstanding items

---

## 11. Completion

A story is complete only when:

- all checks pass
- definition of done is satisfied
- handoff is clear

---

## Loopback Rule

If any stage fails:

- work returns to Builder
- findings must be explicit
- rework must be targeted

Failure is part of the process, not a breakdown of it.

---

## Handoff Rules

Every handoff must include:

- current state
- what changed
- validation status
- known risks
- next step

No implicit knowledge transfer.

---

## Execution Principles

- plan first, then act
- make uncertainty visible
- keep changes small
- protect scope
- record decisions
- surface risk early
- maintain working context

---

## Workflow Integrity

This workflow must be followed.

If steps are skipped:

- quality drops
- risk increases
- traceability is lost
- rework increases

Consistency is the goal.