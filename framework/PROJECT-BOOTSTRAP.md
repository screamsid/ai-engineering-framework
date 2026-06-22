# Project Bootstrap Operating Model

Project Bootstrap is the deterministic entry point for AI-assisted engineering work.

Its purpose is simple:

> A new engineering agent should be able to join a repository, load the correct operating context, and behave consistently without the user repeating governance, Git, security, testing, memory, or project hygiene instructions.

This document defines the minimum complete bootstrap capability for projects using the AI Engineering Framework.

---

## Outcome

A project using this framework should allow a user to say:

```text
Bootstrap this project using the AI Engineering Framework.
```

The agent must then:

1. Load the project bootstrap manifest.
2. Load the assigned project profile.
3. Load the required framework skills.
4. Load the required project skills.
5. Load relevant project memory.
6. Confirm the working mode.
7. Check Git state before changing files.
8. Work only within the permitted workspace.
9. Plan the smallest safe change.
10. Implement the task.
11. Review the output.
12. Update task state and validated memory.
13. Stop at confidence gates when required.

The agent must not choose its own operating context. The project defines it.

---

## Core Principle

### Deterministic bootstrap

Agents do not decide what they need to load.

The project declares:

- profile
- mode
- required skills
- project memory sources
- workspace boundaries
- confidence gates
- Git rules
- review rules

The agent executes that declaration.

This is intentionally similar to role-based access control. A person does not invent their own role when joining a team. The role defines responsibilities, permissions, and expected behaviours.

---

## Framework, Project, Task

The model has three layers.

### Framework layer

The framework provides reusable engineering behaviours:

- bootstrap discipline
- planning
- Git hygiene
- secure coding
- testing
- documentation
- review
- memory management
- confidence gates
- workspace hygiene
- promotion rules

The framework must remain technology-agnostic. It should not contain project-specific Cloudflare, Terraform, AWS, Cisco, or product knowledge.

### Project layer

The project defines local context:

- project profile
- language and tooling
- architecture
- folder structure
- project-specific skills
- domain rules
- naming conventions
- local memory
- local task state
- local working modes

Project profiles are owned by the project. The framework provides the bones, not the project-specific implementation.

### Task layer

The task defines the current outcome only.

A task should not restate Git, security, testing, memory, workspace, or review rules. Those are bootstrap responsibilities.

---

## Required Project Files

A project adopting this bootstrap model should include the following durable files.

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

These files are not placeholders. They must contain enough information for an agent to operate immediately.

Transient AI files belong in ignored workspace paths such as:

```text
.ai/scratch/
.ai/cache/
.ai/runs/
.ai/tmp/
.ai/sandbox/
.ai/research/
.ai/experiments/
```

Durable project memory and task state may be committed when useful. Secrets, real customer data, API responses, logs, and generated backups must not be committed.

---

## Bootstrap Manifest

The project bootstrap manifest is the root instruction file.

Recommended path:

```text
.ai/bootstrap.yaml
```

Minimum usable structure:

```yaml
version: 1

project:
  name: example-project
  framework_version: v0.5

agent:
  default_profile: project-engineer
  response_style: concise
  require_review: true
  require_task_ledger_update: true

mode:
  default: production
  allowed:
    - research
    - sandbox
    - prototype
    - production
    - maintenance

profile:
  file: .ai/project-profile.yaml
  agent_may_select_profile: false

workspace:
  durable_ai_paths:
    - .ai/AGENTS.md
    - .ai/bootstrap.yaml
    - .ai/project-profile.yaml
    - .ai/current-task.md
    - .ai/task-ledger.md
    - .ai/memory/project-memory.md
  transient_ai_paths:
    - .ai/scratch/
    - .ai/cache/
    - .ai/runs/
    - .ai/tmp/
    - .ai/sandbox/
    - .ai/research/
    - .ai/experiments/

memory:
  load:
    - .ai/memory/project-memory.md
  update_policy: validated-only
  agent_may_create_memory_without_review: false

skills:
  framework:
    - bootstrap
    - planning
    - git
    - secure-coding
    - testing
    - documentation
    - reviewing
    - memory-management
    - confidence-gates
    - workspace-hygiene
    - promotion
  project:
    - defined-in-project-profile

git:
  require_status_check_before_changes: true
  require_feature_branch_for_production_changes: true
  never_commit:
    - secrets
    - .env
    - raw-api-responses
    - customer-data
    - generated-backups
    - transient-ai-workspace

confidence:
  stop_below: 70
  require_user_review_below: 90
  allow_autonomous_documentation_changes_above: 90
  allow_autonomous_code_changes_above: 95

review:
  required: true
  update_memory_after_review: true
  update_task_ledger_after_review: true
```

---

## Project Profile

The project profile composes framework behaviours with project-specific details.

Recommended path:

```text
.ai/project-profile.yaml
```

Example:

```yaml
profile:
  name: project-engineer
  owner: project
  agent_may_modify_profile: false

extends:
  framework_profile: software-engineer

project_context:
  language: python
  package_manager: poetry
  test_runner: pytest
  formatter: ruff
  type_checker: mypy
  primary_domain: cloudflare-configuration-collection

project_skills:
  required:
    - python
    - cloudflare-api
    - json
    - http-api-client
    - configuration-discovery
    - secure-secret-handling

operating_rules:
  - Discovery runs before collection.
  - Collectors must be read-only unless explicitly promoted to restore tooling.
  - API tokens must come from environment variables or secret stores.
  - Raw API responses must not be committed.
  - Generated backups must not be committed unless explicitly sanitised and approved.
  - Tests must not call production APIs by default.
```

The framework informs the structure of this file. The project owns the content.

---

## Working Modes

Each task must run in one mode.

| Mode | Purpose | Production files | Git expectation |
| --- | --- | --- | --- |
| research | Learn, compare, investigate | No writes | No commit expected |
| sandbox | Try APIs, tools, scripts | No writes outside `.ai/sandbox/` unless approved | Usually no commit |
| prototype | Build a contained proof of concept | Feature branch only | Commit if useful |
| production | Implement approved work | Allowed within task scope | Commit expected |
| maintenance | Refactor, test, tidy, document | Allowed within task scope | Commit expected |

Agents must not silently upgrade their own mode. For example, research work must not become production code without explicit promotion.

---

## Promotion Pipeline

Work moves through a deliberate promotion path.

```text
Research
  ↓
Sandbox
  ↓
Prototype
  ↓
Production
```

Promotion requires:

- clear outcome
- review
- validation evidence
- updated task ledger
- memory update only for validated learning
- Git changes scoped to the promoted work

---

## Planner, Engineer, Reviewer, Memory Loop

Every task follows the same loop.

```text
Bootstrap
  ↓
Planner
  ↓
Engineer
  ↓
Reviewer
  ↓
Memory Manager
  ↓
Task Ledger
  ↓
Completion
```

### Planner

The planner identifies:

- desired outcome
- working mode
- relevant project memory
- files likely to change
- smallest safe change
- validation plan
- confidence risks

### Engineer

The engineer performs the work within the declared mode and workspace boundaries.

### Reviewer

The reviewer checks:

- task outcome met
- unrelated changes avoided
- tests or validation completed
- secrets not exposed
- project conventions followed
- confidence rating justified

### Memory Manager

The memory manager updates project memory only when learning is validated and reusable.

Examples of memory-worthy learning:

- confirmed API behaviour
- project architecture decision
- recurring implementation pitfall
- validated testing pattern

Examples that must not become long-term memory:

- unverified guesses
- one-off debug output
- secrets
- raw logs
- temporary experiment notes

---

## Confidence Gates

Confidence controls autonomy.

Recommended gates:

| Confidence | Behaviour |
| --- | --- |
| 95 to 100 | Proceed within assigned mode and task scope |
| 90 to 94 | Proceed with explicit review summary |
| 70 to 89 | Stop before risky changes and ask for review |
| Below 70 | Stop and explain uncertainty |

High-risk areas require stricter gates:

- authentication
- authorisation
- secrets
- destructive operations
- production infrastructure
- restore tooling
- customer data
- billing or contract data

---

## No Placeholder Architecture

A framework or project component should not exist unless it is usable.

Agents must not create empty folders, skeletal documents, or TODO-only files as a substitute for working capability.

Acceptable:

- a complete minimal bootstrap
- a complete current-task file
- a complete project profile
- a complete skill with operating rules

Not acceptable:

- empty `docs/` folders
- `coming soon` documents
- unused scaffolding
- speculative architecture files
- generated structures that are not wired into bootstrap

The framework optimises for adoption, not aspiration.

---

## Adoption Checklist

A project is ready to use bootstrap when:

- `.ai/bootstrap.yaml` exists and is populated
- `.ai/AGENTS.md` exists and defines agent rules
- `.ai/project-profile.yaml` exists and defines local project context
- `.ai/current-task.md` exists and describes the active task
- `.ai/task-ledger.md` exists and tracks work
- `.ai/memory/project-memory.md` exists and contains curated memory rules
- `.gitignore` protects transient AI workspace paths
- the agent can explain its loaded profile before making changes
- the agent can name its current working mode
- the agent can describe its validation and review plan

If any item is missing, the first task is to complete bootstrap before project implementation begins.
