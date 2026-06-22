# Workspace Hygiene Skill

## Purpose

Keep production project artefacts separate from AI working artefacts.

This skill prevents exploratory work, experiments, scratch files, and generated outputs from polluting the core project.

## Required Inputs

- `.ai/bootstrap.yaml`
- `.ai/AGENTS.md`
- `.ai/project-profile.yaml`
- active working mode
- Git state summary
- planned file changes

## Required Behaviour

1. Identify whether the task is research, sandbox, prototype, production, or maintenance.
2. Place temporary work in the correct `.ai` transient path.
3. Keep durable AI state in approved `.ai` durable files.
4. Keep production code in production folders only when the working mode allows it.
5. Avoid creating scratch files in project roots.
6. Avoid creating placeholder folders or documents.
7. Confirm generated artefacts are ignored or explicitly approved before commit.
8. Review the diff before completion.

## Workspace Rules

### Durable AI workspace

May be committed when useful:

- `.ai/AGENTS.md`
- `.ai/bootstrap.yaml`
- `.ai/project-profile.yaml`
- `.ai/current-task.md`
- `.ai/task-ledger.md`
- `.ai/memory/project-memory.md`

### Transient AI workspace

Usually ignored by Git:

- `.ai/scratch/`
- `.ai/cache/`
- `.ai/runs/`
- `.ai/tmp/`
- `.ai/sandbox/`
- `.ai/research/`
- `.ai/experiments/`

### Production workspace

Only modify when the working mode and task scope permit it.

Common examples:

- `src/`
- `tests/`
- `docs/`
- `config/`

## Required Outputs

- workspace_mode
- durable_files_changed
- transient_files_created
- production_files_changed
- hygiene_risk_summary
- cleanup_actions

## Stop Conditions

Pause before completion when:

- scratch files were created outside `.ai`
- generated artefacts are staged unexpectedly
- production files changed during research or sandbox mode
- placeholder files were created
- raw outputs were added to durable memory

## Confidence Guidance

Raise confidence when:

- changes are clearly separated by workspace type
- transient files are ignored
- diff is focused
- no generated outputs are staged

Lower confidence when:

- file locations are inconsistent
- project structure is unclear
- working mode is unclear
- generated outputs are mixed with source files

## Candidate Lessons

Propose memory updates when:

- a project-specific workspace rule is validated
- a recurring pollution pattern is found
- a new ignore rule is needed
- a project folder convention needs documenting
