# Project Bootstrap Operating Model

Project Bootstrap is the deterministic entry point for AI-assisted engineering work.

Bootstrap exists to put a project into a known operating state. It does not contain engineering behaviour.

```text
Projects configure behaviour.
Profiles compose skills.
Skills perform work.
Bootstrap orchestrates.
```

## Outcome

A project using this framework should allow a user to say:

```text
Bootstrap this project using the AI Engineering Framework.
```

The agent must then:

1. Validate the bootstrap manifest.
2. Load the declared framework version.
3. Resolve the framework profile.
4. Resolve the project profile.
5. Load the framework skills declared by the framework profile.
6. Load the project skills declared by the project profile.
7. Load declared project memory.
8. Generate `.ai/bootstrap-report.md`.
9. Refresh `.ai/project-health.yaml`.
10. Report `READY` or stop with a clear validation failure.

The agent must not choose its own operating context. The project declares the active profile by name.

## Bootstrap Flow

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

## Bootstrap Must Not Implement

Bootstrap must not directly perform:

- planning
- reviewing
- documentation
- testing
- Git operations
- memory management
- workspace management
- promotion

Those responsibilities belong to framework skills.

## Required Project Files

```text
.ai/
  AGENTS.md
  bootstrap.yaml
  profiles/
    project-engineer.yaml
  current-task.md
  task-ledger.md
  memory/
    project-memory.md
  bootstrap-report.md
  project-health.yaml
```

Durable project memory and task state may be committed when useful. Secrets, real customer data, API responses, logs, and generated backups must not be committed.

Transient AI files belong in ignored workspace paths such as `.ai/scratch/`, `.ai/cache/`, `.ai/runs/`, `.ai/tmp/`, `.ai/sandbox/`, `.ai/research/`, and `.ai/experiments/`.

## Bootstrap Manifest

Recommended path:

```text
.ai/bootstrap.yaml
```

Minimum profile declaration:

```yaml
version: 2

project:
  name: example-project
  framework_version: v0.5

agent:
  profile: project-engineer
  agent_may_select_profile: false

profiles:
  project_path: .ai/profiles
  framework_path: framework/profiles
  active: project-engineer

bootstrap:
  report: .ai/bootstrap-report.md
  project_health: .ai/project-health.yaml
  validation_skill: bootstrap-validation

skills:
  framework:
    source: resolved-framework-profile
  project:
    source: resolved-project-profile
```

## Framework Profiles

Framework profiles define reusable engineering capability.

Recommended path:

```text
framework/profiles/<profile-name>/profile.yaml
```

Framework profiles must never contain project-specific technologies, vendors, libraries, products, or internal standards.

## Project Profiles

Project profiles compose framework capability with project implementation context.

Recommended path:

```text
.ai/profiles/project-engineer.yaml
```

Bootstrap references profiles by name only:

```yaml
agent:
  profile: project-engineer
```

The agent never selects its own profile.

## Profile-Driven Skill Loading

Bootstrap loads skills from resolved profiles.

```text
bootstrap.yaml
  declares agent.profile
    ↓
.ai/profiles/project-engineer.yaml
  declares framework_profile
  declares project_skills
    ↓
framework/profiles/software-engineer/profile.yaml
  declares framework_skills
    ↓
Bootstrap loads declared skills only
```

If a required skill is missing, bootstrap validation fails.

## Bootstrap Validation

Bootstrap calls the `bootstrap-validation` skill before planning or implementation.

Expected output:

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

If validation fails, bootstrap stops with a clear explanation.

## Bootstrap Report

Bootstrap refreshes `.ai/bootstrap-report.md` with framework version, framework profile, project profile, skills loaded, memory sources, working mode, Git summary, confidence gate, and bootstrap status.

The report must be deterministic.

## Project Health

Bootstrap refreshes `.ai/project-health.yaml` with framework version, active profile, working mode, bootstrap status, review status, confidence, memory health, Git advisory state, and last successful bootstrap.

## Working Modes

| Mode | Purpose | Production files | Git expectation |
| --- | --- | --- | --- |
| research | Learn, compare, investigate | No writes | No commit expected |
| sandbox | Try APIs, tools, scripts | No writes outside `.ai/sandbox/` unless approved | Usually no commit |
| prototype | Build a contained proof of concept | Feature branch only | Commit if useful |
| production | Implement approved work | Allowed within task scope | Commit expected |
| maintenance | Refactor, test, tidy, document | Allowed within task scope | Commit expected |

Agents must not silently upgrade their own mode.

## No Placeholder Architecture

A framework or project component should not exist unless it is usable.

Acceptable:

- a complete minimal bootstrap
- a complete current-task file
- a complete project profile
- a complete skill with operating rules
- a deterministic bootstrap report
- a project health file refreshed by bootstrap

Not acceptable:

- empty `docs/` folders
- `coming soon` documents
- unused scaffolding
- speculative architecture files
- generated structures that are not wired into bootstrap

The framework optimises for adoption, not aspiration.
