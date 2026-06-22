# AI Workspace Template

This template gives a project a usable `.ai` workspace for deterministic agent bootstrap.

It is designed so a new engineering agent can join a project and behave consistently without the user restating Git, security, testing, planning, review, memory, or workspace rules.

---

## What this template provides

```text
.ai/
  AGENTS.md
  bootstrap.yaml
  project-profile.yaml
  current-task.md
  task-ledger.md
  memory/
    project-memory.md
```

These are durable project files. They may be committed when they contain safe project operating context.

Transient AI work should stay in ignored paths:

```text
.ai/scratch/
.ai/cache/
.ai/runs/
.ai/tmp/
.ai/sandbox/
.ai/research/
.ai/experiments/
```

---

## Adoption steps

1. Copy `templates/ai-workspace/.ai/` into the target project root.
2. Update `.ai/bootstrap.yaml` with the project name and default mode.
3. Update `.ai/project-profile.yaml` with the project language, tools, structure, and project skills.
4. Update `.ai/current-task.md` with the first outcome-focused task.
5. Keep `.ai/task-ledger.md` updated after each meaningful task.
6. Add validated reusable learning to `.ai/memory/project-memory.md` only after review.
7. Add the transient `.ai` paths to the project `.gitignore`.

---

## First command to give an agent

```text
Bootstrap this project using the AI Engineering Framework. Read `.ai/bootstrap.yaml`, follow `.ai/AGENTS.md`, load the project profile, confirm the working mode, then plan the current task before making changes.
```

The agent should report:

- loaded profile
- working mode
- loaded skills
- memory sources
- Git state
- planned changes
- validation plan
- confidence gate

---

## Project-owned profiles

The framework defines the bones. The project owns the profile.

That means project-specific skills such as Cloudflare, Terraform, Python, React, Elastic, Cisco, or internal naming rules belong in the project profile or project memory, not in the framework repository.

The framework should not automatically absorb project memory.

Framework improvements should be deliberate, reviewed changes.

---

## Working modes

Use these modes to avoid polluting the production project.

| Mode | Use when | Output location |
| --- | --- | --- |
| research | comparing, reading, investigating | `.ai/research/` |
| sandbox | trying APIs or disposable scripts | `.ai/sandbox/` |
| prototype | building a contained proof of concept | feature branch, scoped files |
| production | implementing approved work | production project folders |
| maintenance | tidy, refactor, document, test | scoped project folders |

Research and sandbox work must not modify production files unless promoted.

---

## Promotion rule

Nothing moves from research or sandbox into production automatically.

Promotion requires:

- explicit intent
- review
- validation
- confidence rating
- task ledger update
- memory update only for validated learning

---

## No placeholder architecture

Do not add empty folders or files that only say they will be completed later.

Every file created by the agent should have immediate operational value.

The smallest complete usable capability is better than broad unfinished scaffolding.
