# Bootstrap Skill

## Purpose

Load a project into a known operating state before work begins.

This skill makes each new session repeatable and reduces reliance on chat history.

## Required Inputs

- `.ai/bootstrap.yaml`
- `.ai/AGENTS.md`
- `.ai/project-profile.yaml`
- `.ai/current-task.md`
- `.ai/task-ledger.md`
- `.ai/memory/project-memory.md`

## Required Behaviour

1. Read the bootstrap manifest first.
2. Confirm the assigned profile.
3. Confirm the working mode.
4. Load only declared memory sources.
5. Load framework skills from the manifest.
6. Load project skills from the profile.
7. Check Git state before editing.
8. Confirm workspace boundaries.
9. Identify confidence gates before planning.
10. Pause if required bootstrap files are missing or unusable.

## Required Outputs

- loaded_profile
- working_mode
- loaded_skills
- loaded_memory_sources
- git_state_summary
- workspace_boundaries
- confidence_gate_summary
- bootstrap_status

## Stop Conditions

Pause before editing when:

- `.ai/bootstrap.yaml` is missing
- `.ai/AGENTS.md` is missing
- `.ai/project-profile.yaml` is missing
- the profile permits self-selected context
- the working mode is unclear
- Git state contains unexplained existing changes
- confidence gates cannot be determined

## Confidence Guidance

Lower confidence when:

- bootstrap files are incomplete
- project profile conflicts with task scope
- memory appears stale
- workspace boundaries are unclear
- Git state is not clean

## Candidate Lessons

Propose memory updates when:

- a bootstrap rule prevented confusion
- project profile rules need tightening
- a repeated missing context problem is found
- working mode boundaries need clarification
