---
name: memory-feedback-loop
description: Defines the agent feedback loop for finding, reviewing, sanitising, and promoting reusable lessons into durable memory.
---
# Memory Feedback Loop

Framework memory must not be passive.

A mature agent system needs a feedback loop that reviews work, identifies reusable findings, sanitises them, scores confidence, and promotes only safe lessons into durable memory.

## Core Principle

Agents should not only complete work.

Agents should learn safely from completed work.

The learning process must be deliberate, reviewed, and security-aware.

## Memory Reviewer Role

The Memory Reviewer is responsible for analysing completed work and identifying reusable lessons.

The Memory Reviewer must look for:

- repeated mistakes
- successful reusable patterns
- failed approaches
- validation gaps
- security findings
- agent drift
- context management issues
- unclear handoffs
- missing acceptance criteria
- recurring implementation risks
- useful prompt or workflow improvements

## What The Memory Reviewer Must Not Do

The Memory Reviewer must not:

- copy project secrets into framework memory
- promote raw logs
- expose customer or environment details
- store credentials, tokens, IPs, hostnames, or internal architecture
- persist speculative lessons without evidence
- promote one-off noise as framework guidance

## Feedback Loop Flow

1. Work is completed by normal agent roles
2. Reviewer and Security Reviewer complete their checks
3. Memory Reviewer inspects the task outcome
4. Candidate lessons are extracted
5. Sensitive details are removed
6. Lessons are converted into reusable patterns
7. Confidence rating is assigned
8. Promotion decision is made
9. Accepted lessons are written into the correct memory layer
10. Rejected or uncertain lessons remain in project notes only

## Candidate Lesson Format

Use this format when proposing a memory item:

```markdown
## Candidate Lesson

### Source
<project/task/reference without sensitive detail>

### Finding
<what was learned>

### Reusable Pattern
<abstracted lesson that can help future work>

### Security Review
<sanitisation performed and remaining concerns>

### Applicability
<where this lesson applies>

### Confidence
Rating: High / Medium / Low
Score: 0-100%
Reason: <evidence-based reason>

### Promotion Decision
Promote / Keep project-local / Reject / Needs more evidence
```

## Promotion Rules

A lesson may be promoted into framework memory only when:

- it is reusable across projects
- it has been sanitised
- it does not expose sensitive information
- it is supported by evidence
- confidence is stated
- applicability is clear

## Memory Destinations

| Destination | Use When |
| --- | --- |
| Project Memory | Lesson is useful only inside one project |
| Framework Memory | Lesson is reusable across projects |
| Security Standards | Lesson changes secure operating practice |
| Testing Standards | Lesson changes validation expectations |
| Skills | Lesson improves a repeatable skill workflow |
| Backlog | Lesson suggests future improvement but is not ready |

## Review Cadence

Memory review should happen:

- after meaningful task completion
- after incidents or defects
- after failed validations
- after security findings
- after major architecture decisions
- before release where lessons were discovered

## False Learning Control

Not every finding is true.

The Memory Reviewer must guard against:

- model misdiagnosis
- coincidence mistaken for cause
- incomplete evidence
- stale assumptions
- overfitting to one project
- promoting workarounds as standards

Low-confidence findings must not be promoted into framework memory.

## Completion Rule

A meaningful task is not fully closed until the agent has considered whether any reusable lesson should be captured.

No useful lesson should remain trapped only in conversation context.
