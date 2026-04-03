---
name: git-policy
description: This defines the required git discipline for all work using this framework.
---
# Git Policy

This defines the required git discipline for all work using this framework.

The goal is to ensure:

- traceability
- reviewability
- rollback safety
- clear history
- consistent delivery

---

## Core Principles

Git history must:

- explain what changed
- explain why it changed
- support safe rollback
- support review without guesswork

If the history is unclear, the work is not complete.

---

## Branching

- one story or change stream per branch
- no mixing unrelated work in a branch

### Branch Naming

Branches must be:

- descriptive
- traceable to the story or task
- consistent

### Example Patterns

- feature/story-012-add-rate-parser
- fix/story-019-harden-auth-check
- chore/story-021-update-framework-docs

Project-specific rules can be defined in the project profile.

---

## Commits

Commits must be:

- small
- focused
- logically grouped
- easy to review

### Rules

- one logical change per commit where possible
- do not bundle unrelated changes
- do not create large “catch-all” commits

---

## Commit Messages

Commit messages must explain:

- why the change was made
- not just what changed

### Good Example

"Add validation for API response to prevent null rate parsing failure"

### Bad Example

"Fix stuff"

---

## Commit Frequency

Prefer:

- multiple small commits

Avoid:

- one large commit at the end of work

Small commits improve:
- review
- rollback
- traceability

---

## Rollback Safety

All changes must be:

- easy to isolate
- easy to revert

If rollback would be difficult:
- the change is too large
- or not properly structured

---

## Tags

Tags must be used for:

- framework versions
- release points
- significant milestones
- safe rollback checkpoints (where needed)

### Tag Rules

- tags must be meaningful
- tags must be consistent
- tags must align with versioning strategy

---

## Pull Requests (if used)

Pull requests must include:

- summary of change
- scope
- risks
- validation performed
- security considerations (if relevant)
- rollback considerations

Pull requests are not just a formality.  
They are part of traceability.

---

## .gitignore Hygiene

Every project must maintain a strict `.gitignore` file.

You must ensure the following are NEVER tracked by Git:

- passwords, tokens, API keys, or usernames
- `.env` files or local credentials configurations
- runtime logs, data dumps, or packet captures
- data produced from test runs or test outputs

If sensitive data or test outputs are accidentally tracked, they must be purged from the repository history, not just deleted in a subsequent commit.

---

## Prohibited Patterns

Do not:

- commit directly to protected branches
- create vague commit messages
- bundle unrelated changes together
- skip commits and push large change sets
- introduce silent behavioural changes
- bypass review for convenience

---

## Audit Alignment

Git history must align with the audit log.

For meaningful changes:

- commits should be traceable to audit entries
- audit entries should reference commits where possible

---

## Working Rule

If someone cannot understand the change by reading the git history:

- the git history is not good enough

---

## Enforcement

If git standards are not met:

- the work is not ready
- changes must be restructured before completion

Git discipline is not optional. It is required for safe delivery.