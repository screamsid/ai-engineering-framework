---
name: agent-adherence
description: Standards for keeping agents aligned to framework rules during execution.
---
# Agent Adherence

Agents and LLMs can drift during work.

They may begin correctly, then gradually forget:

- role boundaries
- framework rules
- validation requirements
- security expectations
- scope limits
- handoff standards
- confidence reporting

This document defines controls to keep agents on point throughout execution.

## Core Principle

Framework rules must be actively reinforced during work.

Do not assume an agent will remember all rules because they appeared at the start of a task.

## Adherence Model

Agent adherence uses five controls:

1. Role anchoring
2. Task preflight
3. Execution checkpoints
4. Self-audit before handoff
5. Reviewer enforcement

## 1. Role Anchoring

Every agent must start by identifying its role and operating boundaries.

Example:

```markdown
Role: Builder
Scope: Implement approved plan only
Must Follow: Core rules, testing standards, security standards, confidence ratings
Must Not Do: Expand scope, skip validation, make undocumented assumptions
```

Role anchoring keeps the agent grounded in what it is allowed to do.

## 2. Task Preflight

Before meaningful work begins, the agent must confirm:

- task objective
- role being performed
- relevant framework documents
- known constraints
- acceptance criteria
- validation requirements
- security considerations
- expected outputs

If any critical item is missing, the agent must surface the gap.

## 3. Execution Checkpoints

For longer tasks, the agent must periodically check alignment.

A checkpoint should ask:

```markdown
Am I still inside the approved scope?
Am I following my assigned role?
Have I introduced any hidden assumption?
Have I changed behaviour without documenting it?
Have I preserved rollback safety?
Have I updated context or audit notes where required?
Is validation still appropriate for the risk?
```

Checkpoints should be lightweight.

They exist to prevent drift, not slow delivery.

## 4. Self-Audit Before Handoff

Before handing work over, the agent must perform a self-audit.

Required format:

```markdown
## Agent Self-Audit

Role followed: Yes / No / Partial
Scope maintained: Yes / No / Partial
Assumptions documented: Yes / No / N/A
Validation completed: Yes / No / Partial
Security considered: Yes / No / N/A
Context updated: Yes / No / N/A
Confidence included: Yes / No
Known gaps stated: Yes / No
```

If any answer is No or Partial, the agent must explain why.

## 5. Reviewer Enforcement

Reviewers must check not only the output, but whether the agent obeyed the framework.

Reviewer checks must include:

- did the agent stay in role?
- did it follow the approved plan?
- did it skip required validation?
- did it hide assumptions?
- did it update context appropriately?
- did it provide confidence and gaps?
- did it introduce process or memory drift?

## Rule Refresh Blocks

For long or complex work, the harness should re-inject a short rule refresh block before major phases.

Example:

```markdown
Framework Refresh:
- Stay within current role.
- Do not expand scope silently.
- Validate meaningful changes.
- State assumptions and gaps.
- Include confidence rating.
- Update durable context when lessons matter.
```

This should be short.

Do not re-inject the full framework unless necessary.

## Stop Conditions

An agent must stop and escalate when:

- the task is unclear
- acceptance criteria are missing
- the agent is about to exceed scope
- security risk is material and unresolved
- validation cannot be performed
- framework rules conflict
- required context is missing

Stopping is not failure.

Continuing blindly is failure.

## Anti-Pattern: Prompt Stuffing

Do not solve adherence by dumping the entire framework into every prompt.

That creates:

- bloated context
- lower signal
- higher cost
- weaker attention
- more drift

Instead, inject only the relevant rules for the role and task.

## Minimal Rule Card

Each agent should receive a small rule card.

Example:

```markdown
Role: <Planner / Builder / Reviewer / Security Reviewer / Git Manager / Release Manager / Memory Reviewer>
Task: <current task>
Scope: <allowed work>
Relevant Rules: <short list>
Required Outputs: <short list>
Stop If: <short list>
```

## Adherence Scoring

Reviewers may score adherence:

| Score | Meaning |
| --- | --- |
| 90-100% | Strong adherence, no material gaps |
| 70-89% | Mostly aligned, minor gaps |
| 50-69% | Partial adherence, rework likely needed |
| 0-49% | Poor adherence, output should not be trusted |

Adherence score is separate from technical confidence.

An output can be technically correct but still fail framework adherence.

## Completion Rule

A task is not complete if the agent produced useful work while materially ignoring the framework.

Useful output without process adherence is still operational risk.
