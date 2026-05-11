---
name: context-management
description: Standards for managing active context, working context, durable memory, and handoffs.
---
# Context Management

Context is a limited operational resource.

The framework must keep active context short, accurate, and useful while preserving important learnings in durable documentation.

## Core Rule

Conversation context is not trusted durable memory.

If something matters beyond the current task, write it down in the correct project or framework document.

## Context Layers

| Layer | Purpose | Lifetime | Storage |
| --- | --- | --- | --- |
| Active Context | Immediate task execution | Minutes or hours | Current session |
| Working Context | Current project state | Days or weeks | Project working context |
| Project Knowledge | Stable project decisions and learnings | Months | Project docs |
| Framework Knowledge | Cross-project standards and operating rules | Long-term | Framework docs |
| Lessons Learned | Reusable mistakes, fixes, and patterns | Long-term | Lessons learned docs |

## What Must Be Preserved

Preserve information that helps future agents avoid relearning.

Examples:

- decisions made
- constraints discovered
- validation outcomes
- failed approaches
- known pitfalls
- architecture choices
- security assumptions
- accepted risks
- project-specific rules
- reusable implementation patterns

## What Must Not Be Preserved

Do not preserve noise.

Avoid storing:

- temporary thoughts
- outdated assumptions
- duplicated notes
- irrelevant logs
- abandoned ideas without value
- conversational filler
- stale task detail after completion

## Context Compression

When context grows, summarise it.

A useful context summary must include:

- current goal
- current state
- completed work
- decisions made
- files changed
- validation performed
- known gaps
- next recommended action
- confidence rating

## Handoff Standard

Every handoff should be short, explicit, and usable without reading the entire conversation.

Use this format:

```markdown
## Handoff

### Current State
<where the work is up to>

### Completed
<what has been done>

### Decisions
<important choices made>

### Validation
<tests or checks completed>

### Known Gaps
<what is missing or uncertain>

### Next Action
<recommended next step>

### Confidence
Rating: High / Medium / Low
Score: 0-100%
Reason: <evidence-based reason>
```

## Stale Context Handling

If documentation conflicts with conversation context:

1. prefer the latest durable project documentation
2. check audit logs or commits where possible
3. explicitly call out the conflict
4. do not silently choose one version

## Agent Instructions

Agents must:

- keep active context short
- update durable context when lessons matter
- avoid repeating large context blocks unnecessarily
- record decisions close to the relevant project area
- remove or mark obsolete context where possible
- never rely on memory alone for critical project rules

## Completion Rule

A task is not complete if important learnings remain only in conversation context.
