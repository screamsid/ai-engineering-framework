---
name: skills
description: Reusable capability packs for specialised agent tasks.
---
# Skills

Skills are reusable operational capability packs.

They exist to:

- reduce relearning
- standardise execution
- improve consistency
- improve validation quality
- improve security outcomes
- reduce context size

## Core Principle

Do not solve the same operational problem differently every time.

If a workflow becomes common:

- standardise it
- document it
- reuse it

## Skill Structure

Each skill should define:

- purpose
- scope
- inputs
- outputs
- validation expectations
- security considerations
- confidence requirements
- escalation conditions

## Recommended Skill Packs

### Secure Coding

Purpose:
- enforce secure implementation practices

Examples:
- input validation
- least privilege
- secret handling
- dependency review
- injection prevention
- subprocess safety
- logging safety
- secure defaults

### Smoke Testing

Purpose:
- verify core functionality quickly and safely

Examples:
- service startup
- endpoint response
- CLI execution
- configuration load
- authentication flow

### Functional Testing

Purpose:
- validate expected behaviour

Examples:
- workflow execution
- parser validation
- state transitions
- business logic

### Validation Testing

Purpose:
- ensure implementation matches requirements and acceptance criteria

Examples:
- acceptance validation
- output verification
- architecture alignment
- rollback verification

### Security Review

Purpose:
- identify security weaknesses and unsafe assumptions

Examples:
- attack surface review
- abuse path analysis
- trust boundary review
- external integration review
- dependency analysis

### Git Hygiene

Purpose:
- maintain rollback-safe repository quality

Examples:
- branch discipline
- commit quality
- isolated changes
- audit alignment
- release readiness

## Capability Routing

Agents should route tasks to the most appropriate capability.

Examples:

| Task | Preferred capability |
| --- | --- |
| Security review | High-reasoning or specialised security model |
| Large architecture review | High-context planning model |
| Repetitive implementation | Low-cost builder model |
| Validation reporting | Structured reviewer workflow |
| Dependency analysis | Security-focused skill pack |

## Confidence Requirements

Every skill execution must include:

- validation performed
- confidence rating
- known gaps
- recommended next action

## Completion Rule

A skill pack is incomplete if:

- outputs are inconsistent
- validation is unclear
- security expectations are undefined
- confidence reporting is missing
