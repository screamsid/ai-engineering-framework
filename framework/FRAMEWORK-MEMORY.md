---
name: framework-memory
description: Durable institutional memory standards for agent systems.
---
# Framework Memory

Framework memory exists to preserve important operational learnings across projects without leaking sensitive information.

The purpose is not to retain project secrets.

The purpose is to retain:

- reusable lessons
- operational patterns
- failure modes
- validation improvements
- security learnings
- architecture guidance
- anti-patterns
- agent workflow improvements

## Core Principle

Learnings must be abstracted before being promoted into framework memory.

Do not copy raw project detail into shared memory.

## Separation Model

| Memory Layer | Scope | Sensitivity |
| --- | --- | --- |
| Active Context | Current task | High |
| Project Memory | Single project | Medium to High |
| Framework Memory | Cross-project reusable knowledge | Low |

## What Belongs In Framework Memory

Safe reusable operational learnings.

Examples:

- validation workflows
- context compression patterns
- security review checklists
- known hallucination patterns
- effective testing strategies
- architecture review lessons
- dependency risk patterns
- reusable guardrails
- workflow improvements
- prompt structure improvements
- drift prevention patterns
- rollback lessons

## What Must Never Enter Framework Memory

Never store:

- credentials
- secrets
- tokens
- API keys
- internal IPs
- customer data
- confidential architecture
- sensitive infrastructure detail
- proprietary source code
- private incident data
- sensitive logs
- personal data
- vendor-sensitive configurations

## Abstraction Rule

Before promoting a lesson into framework memory:

1. remove project-specific identifiers
2. remove customer-specific detail
3. remove sensitive operational information
4. convert the lesson into a reusable pattern
5. preserve the operational value only

## Example

Bad:

"Customer X exposed AWS keys in repository Y after migration Z."

Good:

"Migration workflows should include automated secret scanning before merge approval."

## Security Boundary

Framework memory is guidance memory, not operational data storage.

It should teach:

- how to think
- how to validate
- how to reduce risk
- how to avoid repeat mistakes

It should not expose:

- who
- where
- what infrastructure
- what secrets
- what customers

## Review Requirement

All framework memory additions should be reviewed for:

- reusable value
- abstraction quality
- accidental data leakage
- security impact
- operational usefulness

## Confidence Requirement

Lessons promoted into framework memory should include:

- confidence rating
- evidence basis
- known limitations
- applicability scope

## Anti-Pattern Rule

Do not allow framework memory to become:

- a dumping ground
- a copy of project context
- unreviewed operational notes
- stale undocumented assumptions

## Completion Rule

A cross-project lesson is not fully institutionalised until:

- it is abstracted
- reviewed
- documented safely
- reusable by future agents
