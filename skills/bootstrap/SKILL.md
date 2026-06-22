# Bootstrap Skill

## Purpose

Operate bootstrap as a deterministic orchestration layer.

Bootstrap does not plan, review, test, document, manage memory, manage Git, manage the workspace, or promote work. It validates the declared operating context, resolves profiles, loads declared skills and memory, writes deterministic bootstrap state, then hands execution to the skills declared by the active profile.

## Required Inputs

- `.ai/bootstrap.yaml`
- `.ai/AGENTS.md`
- `.ai/profiles/<profile-name>.yaml`
- `.ai/current-task.md`
- `.ai/task-ledger.md`
- `.ai/memory/project-memory.md`
- framework profile declared by the project profile
- framework skills declared by the resolved framework profile
- project skills declared by the resolved project profile

## Orchestration Flow

Bootstrap must run this sequence and stop on validation failure:

```text
Validate
  ↓
Load Framework Version
  ↓
Resolve Framework Profile
  ↓
Resolve Project Profile
  ↓
Load Framework Skills
  ↓
Load Project Skills
  ↓
Load Project Memory
  ↓
Generate Bootstrap Report
  ↓
Update Project Health
  ↓
Ready
```

## Delegated Responsibilities

| Responsibility | Skill owner |
| --- | --- |
| Validation | `bootstrap-validation` |
| Planning | `planning` |
| Review | `reviewing` |
| Documentation | `documentation` when available in the active profile |
| Testing | `testing` when available in the active profile |
| Git hygiene | `git` when available in the active profile |
| Memory updates | `memory-management` |
| Workspace boundaries | `workspace-hygiene` |
| Promotion | `promotion` |
| Confidence decisions | `confidence-gates` when available in the active profile |

If a delegated skill is declared but missing, bootstrap fails validation instead of implementing that behaviour itself.

## Required Behaviour

1. Read `.ai/bootstrap.yaml` first.
2. Confirm the agent profile name declared by `agent.profile`.
3. Resolve `.ai/profiles/<agent.profile>.yaml`.
4. Resolve the framework profile named by the project profile.
5. Load only framework skills declared by the framework profile.
6. Load only project skills declared by the project profile.
7. Load only memory sources declared by the bootstrap manifest.
8. Call `bootstrap-validation` before any planning or implementation.
9. Generate `.ai/bootstrap-report.md` deterministically.
10. Refresh `.ai/project-health.yaml` deterministically.
11. Report `READY` only after validation passes.

## Required Outputs

- framework_version
- framework_profile
- project_profile
- framework_skills_loaded
- project_skills_loaded
- memory_sources_loaded
- working_mode
- git_summary
- confidence_gate
- bootstrap_status

## Stop Conditions

Stop before planning or implementation when:

- `.ai/bootstrap.yaml` is missing
- `.ai/AGENTS.md` is missing
- the declared project profile is missing
- the framework profile is missing
- a declared required skill is missing
- the project allows the agent to choose its own profile
- the working mode is unclear
- memory sources are missing or outside the declared boundary
- Git state cannot be summarised
- confidence gates cannot be determined
- `.ai/bootstrap-report.md` or `.ai/project-health.yaml` cannot be refreshed

## Confidence Guidance

Raise confidence when profiles resolve by name, all declared skills exist, project memory loads cleanly, Git state is known, workspace boundaries are explicit, and bootstrap state is refreshed.

Lower confidence when framework and project profile declarations conflict, project profile contains framework-level behaviour, required skills are missing, memory appears stale, or workspace boundaries are unclear.

## Candidate Lessons

Propose memory updates when bootstrap validation exposes a repeated profile, skill, or memory issue, or when a framework capability should be moved from bootstrap into a skill.
