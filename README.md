# AI Engineering Framework

A reusable operating model for AI-assisted and multi-agent software delivery.

This repository is the source of truth for how projects should be planned, built, reviewed, secured, tested, handed over, and improved when using AI agents in engineering workflows.

It is designed to be reused across multiple project types and refined over time, so teams do not need to rebuild process, standards, or working patterns for every new repo.

## Why This Exists

Without structure, AI-assisted delivery tends to:

- repeat the same setup in every session
- forget working practices unless reminded
- mix planning, implementation, and review into one pass
- make hidden assumptions
- drift from agreed standards
- produce weak handoffs
- create large hard-to-review changes
- lose useful project memory between sessions

This framework exists to reduce that.

It moves stable engineering guidance out of temporary chat context and into a reusable, versioned framework that can be applied across projects.

The goal is simple:

- more consistency
- better handoffs
- stronger review and rollback
- less repeated instruction
- lower context waste
- safer delivery

## What This Framework Is

This is not just a prompt library.

It is a reusable engineering framework made up of:

- core rules
- workflow definitions
- role instructions
- engineering, security, git, and testing standards
- project templates
- operating modes
- project presets
- examples and guidance

Together, these create a structured operating model that can be applied to real projects and improved over time.

## Core Principles

### Plan before action
No meaningful implementation should begin until the task is understood and a plan exists.

### No hidden assumptions
If something is unclear, the gap must be identified explicitly.

### Small safe changes
Work should be broken into small, reviewable, reversible steps.

### Reuse before rebuild
Existing modules, patterns, and docs should be checked before creating something new.

### Security is first class
Security must be part of planning, implementation, review, and release.

### Validation is mandatory
Every meaningful change must be tested at a level proportionate to risk.

### New ideas go to the backlog
Out-of-scope ideas should be captured, not silently folded into current delivery.

### Handoffs must be explicit
If work is passed on, the current state must be clear.

### Git should protect rollback
Small commits, clean history, and tagging support safe change management.

### The framework is a product
This repo should evolve deliberately, be versioned properly, and improve with use.

## Framework Layers

This framework separates information into layers so agents do not have to relearn the wheel every session.

### 1. Core framework
Stable rules that apply across most projects.

Examples:
- core rules
- workflow
- git policy
- security standards
- testing standards
- definition of done

### 2. Project profile
Project-specific overlay information.

Examples:
- project type
- languages and frameworks
- deployment model
- branch naming
- testing expectations
- security sensitivity
- architecture constraints

### 3. Working context
Short-lived operational memory for the current state of a project.

Examples:
- current story
- active branch
- priorities
- open risks
- blockers
- latest meaningful change
- recommended next step

This layered model reduces repeated setup, improves continuity, and keeps active context focused on current work.

## Multi-Agent Model

This framework supports role separation so planning, implementation, review, security checking, git hygiene, and release readiness do not collapse into one vague blob.

Default team roles:

- Planner
- Builder
- Reviewer
- Security Reviewer
- Git Manager
- Release Manager

Not every project needs every role every time, which is why the framework also supports operating modes.

## Operating Modes

### Lean
For smaller scripts, prototypes, and lower-risk work.

Typical roles:
- Planner
- Builder
- Reviewer

### Standard
For most internal tools, automation, services, and engineering projects.

Typical roles:
- Planner
- Builder
- Reviewer
- Security Reviewer
- Git Manager

### Full
For higher-risk, externally exposed, production-critical, or more formal delivery workflows.

Typical roles:
- Planner
- Builder
- Reviewer
- Security Reviewer
- Git Manager
- Release Manager

The point of modes is to keep the framework strong without overloading smaller projects.

## Project Presets

To make adoption easier, the framework is intended to support reusable presets for common project types, such as:

- Python automation
- web app
- API service
- infrastructure automation
- security tool
- data tool

A preset provides sensible defaults that can then be tailored in the project profile.

## What It Solves

### Repeated context setup
Stable guidance lives here instead of being re-explained in every session.

### Weak project memory
Project profile, working context, backlog, and audit structures preserve useful state outside the active context window.

### Unclear handoffs
Structured roles and handoff patterns reduce hidden context.

### Scope drift
Backlog discipline and role separation stop current work being derailed by new ideas.

### Poor traceability
Git discipline, audit logging, and clear workflows improve reviewability and rollback readiness.

### Inconsistent quality
Shared standards for engineering, testing, security, and release raise the baseline across projects.

## Repository Structure

    .
    ├── README.md
    ├── VERSION.md
    ├── framework/
    │   ├── AGENTS.md
    │   ├── CORE-RULES.md
    │   ├── WORKFLOW.md
    │   ├── ENGINEERING-STANDARDS.md
    │   ├── SECURITY-STANDARDS.md
    │   ├── GIT-POLICY.md
    │   ├── TESTING-STANDARDS.md
    │   └── DEFINITION-OF-DONE.md
    ├── roles/
    │   ├── planner.md
    │   ├── builder.md
    │   ├── reviewer.md
    │   ├── security-reviewer.md
    │   ├── git-manager.md
    │   └── release-manager.md
    ├── templates/
    │   ├── STORY-TEMPLATE.md
    │   ├── HANDOFF-TEMPLATE.md
    │   ├── PROJECT-PROFILE.md
    │   ├── WORKING-CONTEXT.md
    │   ├── BACKLOG.md
    │   └── AUDIT-LOG.md
    ├── modes/
    │   ├── lean.md
    │   ├── standard.md
    │   └── full.md
    ├── presets/
    │   ├── python-automation.md
    │   ├── web-app.md
    │   ├── infra-automation.md
    │   └── security-tool.md
    └── examples/

## How to Use This Framework

Because this framework uses standard YAML frontmatter for all core rules, workflows, and modes, modern agentic IDEs (Cursor, Claude Code, GitHub Copilot Workspace, etc.) natively ingest these files as "Skills" or "Rules." 

Here is how to seamlessly inject this operating model into any target project:

### 1. Add as a Submodule (Recommended)
Add this repository as a submodule into your new project's `.agents/` or `.cursor/` directory. This ensures the semantic indexer automatically loads all rules and constraints:

```bash
git submodule add -b main <your-framework-repo-url> .agents/ai-engineering-framework
```

### 2. Set Global Agent Rules
To enforce the framework passively across an entire project, reference it in your `.cursorrules` or `.claudecode` file within your project root:

```markdown
# Agent Instructions
For this project, you must strictly follow the AI Engineering Framework:
- Start all tasks by cross-referencing `.agents/ai-engineering-framework/framework/WORKFLOW.md`
- Always act in the `builder` role when coding: `.agents/ai-engineering-framework/roles/builder.md`
- Assume you are operating under `.agents/ai-engineering-framework/modes/standard.md`.
```

### 3. Copy the Project Templates
At minimum, copy the local project templates into your target repo:

- `PROJECT-PROFILE.md`
- `WORKING-CONTEXT.md`
- `BACKLOG.md`
- `AUDIT-LOG.md`

### 4. Choose an Operating Mode
Select lean, standard, or full based on project risk and complexity.

### 5. Choose a Project Preset if useful
Use a preset that matches the project type, then tailor it.

### 5. Define the project overlay
Fill in project-specific details such as:

- technical stack
- branch naming
- testing expectations
- architecture constraints
- security sensitivity
- release and tagging expectations

### 6. Work story by story
Use the framework to drive:
- story review
- planning
- implementation
- validation
- review
- security review where required
- git checks
- release readiness

### 7. Feed reusable improvements back into this repo
If a lesson is repeatable, improve the framework here instead of patching each project differently.

## Recommended Adoption Pattern

A practical pattern for most teams:

1. keep this repo as the master framework
2. use project templates in each working repo
3. keep project-specific customisation in the project profile
4. keep current state in working context
5. keep new ideas in backlog
6. keep meaningful changes in audit log
7. feed repeatable improvements back into this framework repo

## What Good Looks Like

Used properly, this framework should give you:

- fewer repeated instructions
- better continuity between sessions
- less context window waste
- cleaner story intake and planning
- smaller safer changes
- clearer handoffs
- better git hygiene
- stronger review and rollback discipline
- more reliable security and testing practices
- easier reuse across future projects

## Maintaining This Repository

Treat this repository like a real product, not a dumping ground.

Framework changes should be:

- deliberate
- reviewable
- documented
- versioned
- tagged where appropriate

Avoid:

- silent behavioural changes
- project-specific clutter in core files
- vague AI philosophy
- process that adds drag without adding value

Keep it sharp. Keep it useful. Trim the fat.

## Versioning

Suggested approach:

- `v0.x` while shaping the model
- `v1.0.0` once the core framework is stable and reusable across projects
- bump versions for meaningful changes
- document changes in `VERSION.md`
- use git tags for framework releases

## Current Direction

Short-term priorities:

- fully populate core framework files
- refine role instructions
- define operating modes clearly
- build out project presets
- test adoption in active projects
- feed lessons back into the framework

## Final Note

This framework should make engineering work easier, clearer, and safer.

If it becomes bloated, ceremonial, or harder to use than the problem it solves, simplify it.

The framework exists to support delivery, not to become the delivery.