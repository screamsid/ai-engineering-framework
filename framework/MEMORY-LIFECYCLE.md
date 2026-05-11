---
name: memory-lifecycle
description: Defines lifecycle, decay, review ownership, and lightweight governance for framework memory.
---
# Memory Lifecycle

Memory must improve the framework without becoming a blocker.

The goal is not process for the sake of process.

The goal is to keep reusable knowledge:

- accurate
- safe
- current
- scoped
- evidence-based
- useful

## Core Principle

Memory is guidance, not bureaucracy.

Memory should help agents move faster and safer.

If memory management slows delivery without reducing risk, it is being applied incorrectly.

## Memory Lifecycle Stages

| Stage | Meaning |
| --- | --- |
| Candidate | A possible lesson has been identified |
| Project-local | Useful inside one project only |
| Promoted | Reusable enough for framework memory |
| Active | Current and recommended guidance |
| Watchlisted | Useful but uncertain, narrow, or needs revalidation |
| Superseded | Replaced by newer guidance |
| Retired | No longer useful or safe to apply |

## Required Memory Metadata

Every promoted memory item should include:

```markdown
### Memory Metadata
Status: Candidate / Project-local / Promoted / Active / Watchlisted / Superseded / Retired
Owner Role: <role responsible for review>
Source Type: Review / Security Review / Testing / Incident / Architecture / Delivery / Drift
Confidence: High / Medium / Low
Score: 0-100%
Evidence: <short evidence basis>
Applicability: <where this applies>
Limitations: <where this should not be applied>
Created: YYYY-MM-DD
Last Reviewed: YYYY-MM-DD
Review Cadence: On change / Quarterly / Six-monthly / Annual / No scheduled review
Expiry: YYYY-MM-DD or Not set
Superseded By: <reference if applicable>
```

## Review Lines

Memory review is multi-role.

Different kinds of memory should be reviewed by the role closest to the risk.

| Memory Type | Primary Reviewer | Secondary Reviewer |
| --- | --- | --- |
| Secure coding lesson | Security Reviewer | Builder |
| Testing lesson | Reviewer | Builder |
| Smoke test lesson | Reviewer | Release Manager |
| Validation lesson | Reviewer | Planner |
| Architecture lesson | Planner | Reviewer |
| Git workflow lesson | Git Manager | Release Manager |
| Release lesson | Release Manager | Git Manager |
| Context lesson | Memory Reviewer | Planner |
| Drift lesson | Memory Reviewer | Reviewer |
| Incident lesson | Security Reviewer or Planner | Memory Reviewer |

## Memory Decay

Memories can become stale.

Decay happens when:

- tools change
- models change
- project patterns change
- security guidance changes
- vendor behaviour changes
- better evidence appears
- a lesson was overfitted to one context

## Decay Signals

A memory should be reviewed when:

- it causes repeated friction
- agents ignore it repeatedly
- it conflicts with newer guidance
- it reduces delivery speed without clear risk reduction
- it is based on weak evidence
- it produces false positives
- it no longer matches current tooling
- it is too broad or too vague

## Lightweight Review Rule

Do not make every memory update a ceremony.

Use proportional governance:

| Change Type | Review Needed |
| --- | --- |
| Typo or wording cleanup | No formal review |
| Clarifying existing guidance | Light review |
| New project-local lesson | Project owner or relevant role |
| New framework-wide lesson | Memory Reviewer plus relevant role |
| Security-impacting lesson | Security Reviewer required |
| Retiring or superseding active guidance | Relevant owner role required |

## Non-Hindrance Rule

Memory controls must not block urgent delivery unless the memory relates to material risk.

For time-sensitive work:

- continue delivery safely
- record candidate lessons later
- do not skip critical security or validation checks
- do not turn memory review into a deployment blocker by default

Memory review is mandatory for learning.

It is not automatically mandatory for release gating unless the project defines it as a gate.

## Confidence And Scope

A memory item must not be applied globally unless its scope supports that.

Confidence must be tied to context.

Example:

```markdown
Confidence: Medium, 70%
Reason: Observed in two Python CLI projects, not yet validated against web applications.
Applicability: Python CLI tools using subprocess execution.
Limitations: Do not apply directly to browser-based applications without review.
```

## Over-Generalisation Control

The Memory Reviewer must prevent one-off findings from becoming universal rules.

Before promotion, ask:

- did this occur more than once?
- is the cause understood?
- is it project-specific?
- does the lesson still help without the original context?
- could this create unnecessary friction?
- is the confidence high enough for broad reuse?

## Retirement And Supersession

A memory should be retired when:

- it is wrong
- it is obsolete
- it creates more harm than value
- it no longer applies
- it is replaced by better guidance

A memory should be superseded when:

- the lesson is still useful historically
- newer guidance is preferred
- retaining history helps explain the change

## Agent Instructions

Agents must:

- use memory as guidance, not blind instruction
- check applicability before applying a lesson
- lower confidence when evidence is weak
- flag stale or harmful memory
- avoid promoting sensitive detail
- avoid turning memory into unnecessary process

## Completion Rule

A memory system is healthy when it helps future agents make better decisions with less context and less relearning.

It is unhealthy when it becomes noisy, stale, over-restrictive, or blocks safe delivery without reducing risk.
