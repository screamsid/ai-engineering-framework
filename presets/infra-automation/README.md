---
name: infrastructure-automation-preset
description: Recommended for infrastructure-as-code, network automation, platform scripts, and change orchestration.
---
# Infrastructure Automation Preset

Recommended for infrastructure-as-code, network automation, platform scripts, and change orchestration.

## Defaults

- Project class: infra-automation
- Risk tier: medium to high
- Preferred mode: standard or full depending on blast radius
- Confidence threshold: medium to high

## Typical Commands

- lint: project-defined
- test: project-defined
- smoke test: safe validation or dry-run mode
- rollback validation: recommended

## Core Focus Areas

- least privilege
- safe defaults
- dry-run support
- rollback thinking
- explicit targeting and scope control
- idempotency
- blast radius awareness
- state drift awareness
- validation before execution
- operational traceability

## Idempotency Expectations

Infrastructure automation should avoid producing different results when run repeatedly against the same intended state.

Projects should:

- validate repeat execution behaviour
- avoid unsafe repeated side effects
- minimise destructive operations
- make intended state explicit

## Blast Radius Awareness

Infrastructure automation should understand and communicate operational impact.

Projects should:

- identify impacted systems
- identify dependency chains
- identify rollback complexity
- identify outage risk
- identify authentication or connectivity risk

High blast-radius work should increase validation depth and confidence requirements.

## State Drift Awareness

Automation should consider:

- expected state
- current state
- drift detection
- partial failure handling
- rollback state consistency

Do not assume environments are already in the expected state.

## Validation Expectations

Infrastructure automation should validate:

- dry-run behaviour
- targeting logic
- rollback behaviour
- authentication handling
- partial failure handling
- idempotency behaviour
- expected state changes
- blast radius assumptions

## Stop Conditions

Stop or escalate when:

- targeting is ambiguous
- rollback is undefined
- blast radius is unclear
- drift cannot be assessed
- credentials or privilege scope are unclear
- confidence is below threshold

## Logging and Auditability

Infrastructure automation should:

- log intent clearly
- record targets
- record execution outcome
- record rollback guidance
- preserve operational traceability

## Memory Candidates

Useful reusable lessons include:

- rollback failures
- drift-handling improvements
- validation improvements
- idempotency patterns
- blast-radius reduction techniques
