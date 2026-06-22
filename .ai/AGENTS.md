# Agent Operating Contract

This repository dogfoods the AI Engineering Framework bootstrap model.

Every engineering agent must read `.ai/bootstrap.yaml`, this file, `.ai/profiles/project-engineer.yaml`, `.ai/current-task.md`, `.ai/task-ledger.md`, and `.ai/memory/project-memory.md` before making changes.

## Non-negotiable rules

1. Do not choose your own operating context.
2. Load the project profile declared in `.ai/bootstrap.yaml`.
3. Work only in the declared working mode.
4. Check Git state before changing files.
5. Do not make unrelated refactors.
6. Do not create placeholder architecture.
7. Do not commit secrets, credentials, raw API responses, customer data, or generated backups.
8. Keep temporary work inside approved `.ai` transient paths.
9. Review your own output before completion.
10. Update the task ledger after meaningful work.
11. Update project memory only with validated reusable learning.
12. Stop when confidence gates require review.

## Framework repository rule

Project-specific behaviour must not be promoted into framework skills unless it is reusable across projects and has been reviewed as framework-level behaviour.
