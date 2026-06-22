# Bootstrap Validation Skill

## Purpose

Validate that a project can be loaded into a deterministic operating state before any planning or implementation begins.

This skill performs validation only. It does not plan, implement, review, test, update memory, or change Git state.

## Required Inputs

- `.ai/bootstrap.yaml`
- `.ai/AGENTS.md`
- `.ai/profiles/<profile-name>.yaml`
- `.ai/current-task.md`
- `.ai/task-ledger.md`
- `.ai/memory/project-memory.md`
- resolved framework profile
- declared framework skills
- declared project skills
- workspace rules
- Git state summary
- confidence gates

## Required Behaviour

1. Validate the bootstrap manifest exists and is parseable.
2. Validate the framework version is declared.
3. Validate `agent.profile` is declared by name.
4. Validate the declared project profile exists under `.ai/profiles/`.
5. Validate the project profile resolves exactly one framework profile.
6. Validate the framework profile exists under `framework/profiles/`.
7. Validate all required framework skills exist.
8. Validate all required project skills are declared by the project profile.
9. Validate declared memory sources exist and are allowed.
10. Validate `.ai/current-task.md` declares a working mode.
11. Validate workspace boundaries are declared.
12. Validate Git state has been checked or explicitly marked unavailable.
13. Validate confidence gates are declared.
14. Return a clear pass or fail result.

## Required Output Format

```text
Bootstrap Validation

✓ Framework
✓ Profiles
✓ Skills
✓ Memory
✓ Workspace
✓ Git

READY
```

If validation fails, replace `READY` with `BLOCKED` and include the smallest clear explanation of what must be corrected.

## Stop Conditions

Return `BLOCKED` when a required bootstrap file is missing, the framework version is missing, the project or framework profile cannot be resolved, a required skill is missing, the agent can self-select a profile, memory paths are missing or unsafe, the working mode is invalid, workspace boundaries are missing, Git state is unknown, or confidence gates are missing.

## Confidence Guidance

Raise confidence when all validation checks pass using explicit configuration. Lower confidence when validation depends on inference, fallback paths, or stale memory.

## Candidate Lessons

Propose memory updates when a validation check prevents an unsafe or inconsistent bootstrap, a recurring bootstrap configuration error is found, or a project needs a clearer profile or memory boundary.
