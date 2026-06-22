# Memory Management Skill

## Purpose

Keep project memory useful, safe, validated, and small enough to remain operational.

Memory management happens after review, not during uncontrolled exploration.

## Required Inputs

- review summary
- validation evidence
- existing project memory
- project profile
- task ledger
- confidence rating

## Required Behaviour

1. Identify candidate learning from the completed task.
2. Classify each candidate as transient, project memory, or framework improvement suggestion.
3. Store project-specific learning only in project memory.
4. Do not sync project memory into the framework automatically.
5. Add only validated, reusable, safe learning.
6. Prefer updating existing memory over duplicating entries.
7. Include confidence and validation source.
8. Remove or mark obsolete memory when new evidence replaces it.

## Required Outputs

- memory_candidates
- memory_decisions
- memory_updates
- rejected_memory_items
- confidence_impact

## Memory Classification

### Transient

Use for temporary notes, experiments, raw findings, and unverified observations.

Store under:

- `.ai/scratch/`
- `.ai/research/`
- `.ai/sandbox/`
- `.ai/experiments/`

### Project Memory

Use for validated project-specific knowledge.

Store under:

- `.ai/memory/project-memory.md`

### Framework Improvement Suggestion

Use when a learning appears reusable across many projects.

Do not update the framework automatically. Record the suggestion for human review.

## Stop Conditions

Do not write memory when:

- learning is unverified
- learning is one-off task state
- the item contains protected information
- the item contains raw external output
- the item belongs in the task ledger instead
- confidence is too low

## Confidence Guidance

Raise confidence when:

- learning is validated by tests
- learning repeated across tasks
- human review confirmed it

Lower confidence when:

- learning is inferred
- validation was partial
- the source is unclear
- it may become stale quickly

## Candidate Lessons

This skill itself should propose framework improvement suggestions when:

- memory becomes noisy
- repeated duplicate entries appear
- project and framework memory boundaries blur
- agents repeatedly forget validated project rules
