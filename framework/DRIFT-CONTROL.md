---
name: drift-control
description: Standards for detecting and controlling operational, architectural, and validation drift.
---
# Drift Control

Long-running agent systems naturally drift over time.

Without explicit controls, systems degrade through:

- scope creep
- architecture drift
- inconsistent validation
- hidden assumptions
- duplicated patterns
- stale context
- operational inconsistency

Drift must be actively managed.

## Types of Drift

### Scope Drift

When implementation expands beyond the approved story.

Examples:

- opportunistic refactors
- unrelated fixes
- silent feature additions
- hidden behavioural changes

### Architecture Drift

When the implementation slowly diverges from intended design.

Examples:

- bypassing shared modules
- duplicated logic
- inconsistent patterns
- breaking established structure

### Validation Drift

When testing and review quality becomes inconsistent.

Examples:

- skipped smoke tests
- weaker review quality
- inconsistent security checks
- unverified assumptions

### Context Drift

When active context diverges from durable project knowledge.

Examples:

- undocumented decisions
- stale assumptions
- contradictory summaries
- relying on memory over documentation

## Required Controls

### Plan Anchoring

All implementation must map back to:

- the approved story
- acceptance criteria
- the execution plan

If work diverges:

- stop
- identify the drift
- update the plan or backlog explicitly

## Validation Consistency

Validation standards must remain consistent across work.

Every meaningful change requires:

- smoke testing
- proportional validation
- explicit confidence rating
- documented gaps

## Architecture Consistency

Agents must:

- reuse established patterns
- avoid unnecessary divergence
- document intentional design changes
- avoid creating duplicate systems

## Drift Detection Questions

Agents should regularly ask:

- are we still solving the original problem?
- has scope expanded silently?
- does this still align with project architecture?
- are validations still appropriate?
- are assumptions now replacing evidence?
- does durable documentation still match reality?

## Escalation Rule

If material drift is detected:

- surface it immediately
- explain the impact
- recommend corrective action
- do not continue silently

## Completion Rule

A task is not complete if:

- implementation drift exists
- validation drift exists
- architecture divergence is undocumented
- project documentation no longer reflects reality
