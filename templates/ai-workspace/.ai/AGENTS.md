# Agent Operating Contract

This project uses the AI Engineering Framework bootstrap model.

Every engineering agent must read this file, `.ai/bootstrap.yaml`, `.ai/project-profile.yaml`, `.ai/current-task.md`, `.ai/task-ledger.md`, and `.ai/memory/project-memory.md` before making changes.

---

## Non-negotiable rules

1. Do not choose your own operating context.
2. Load the project profile declared in `.ai/bootstrap.yaml`.
3. Work only in the declared working mode.
4. Check Git status before changing files.
5. Do not make unrelated refactors.
6. Do not create placeholder architecture.
7. Do not commit secrets, credentials, raw API responses, customer data, or generated backups.
8. Keep temporary work inside approved `.ai` transient paths.
9. Review your own output before completion.
10. Update the task ledger after meaningful work.
11. Update project memory only with validated reusable learning.
12. Stop when confidence gates require review.

---

## Required task loop

Every task follows this loop:

```text
Bootstrap
  ↓
Plan
  ↓
Implement
  ↓
Review
  ↓
Update task ledger
  ↓
Update validated memory
  ↓
Report outcome
```

Skipping review is not allowed.

---

## Working modes

### Research

Use for learning and comparison.

Allowed:

- read files
- create notes in `.ai/research/`
- summarise findings

Not allowed:

- modifying production files
- creating source code outside `.ai/research/`
- promoting findings to memory without validation

### Sandbox

Use for temporary experiments.

Allowed:

- scripts and test probes in `.ai/sandbox/`
- disposable API experiments using mock or safe data

Not allowed:

- committing raw output
- writing to production folders
- using production credentials unless explicitly approved

### Prototype

Use for contained proof of concept work.

Allowed:

- feature branch work
- limited production folder changes within task scope
- tests and documentation for the prototype

Required:

- clear promotion decision before production adoption

### Production

Use for approved implementation.

Allowed:

- scoped source, test, and documentation changes

Required:

- feature branch
- tests or documented validation
- review summary
- task ledger update

### Maintenance

Use for refactoring, tidying, testing, or documentation improvements.

Allowed:

- scoped cleanup
- test improvements
- documentation updates

Required:

- no behaviour changes unless explicitly stated

---

## Git rules

Before changes:

- identify current branch
- check for uncommitted work
- avoid overwriting human changes

During changes:

- keep commits focused
- avoid broad formatting changes unless requested
- avoid unrelated file movement

Before completion:

- review diff
- list files changed
- state validation performed

---

## Security rules

Never store or commit:

- API tokens
- credentials
- `.env` files
- private keys
- certificates
- raw customer data
- raw API responses
- generated backups
- security-sensitive logs

Use environment variables or approved secret stores for secrets.

Tests must default to mocks, fixtures, or safe development accounts.

---

## Memory rules

Project memory is curated engineering knowledge, not a scratchpad.

Add memory only when the learning is:

- validated
- reusable
- project-specific
- safe to store
- useful for future tasks

Do not store guesses, raw outputs, secrets, personal data, or one-off debugging notes.

---

## Completion format

Each completed task should report:

- outcome
- files changed
- validation performed
- confidence rating
- memory updates made or not made
- next recommended task

Keep the response concise.
