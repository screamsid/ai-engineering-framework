# AI Engineering Framework

A reusable engineering operating model for AI-assisted delivery teams.

This repository is the source of truth for how agent-driven engineering work should be planned, implemented, reviewed, secured, tested, and handed off across projects.

## Design philosophy

This framework prioritises:

- clarity over cleverness
- structure over speed
- safety over shortcuts
- reuse over reinvention
- small reversible changes over big risky ones

It is intentionally opinionated to reduce ambiguity and improve consistency across projects.

## What this repo contains

- `framework/` core rules, workflow, standards, and templates
- `roles/` role instructions for the engineering team
- `templates/` project bootstrap files
- `modes/` lean, standard, and full operating modes
- `presets/` project-type defaults
- `examples/` example layouts and usage
- `docs/` guidance for adoption and extension

## Recommended usage

1. Pick an operating mode from `modes/`
2. Pick a project preset from `presets/`
3. Copy the project template from `templates/project-template/` into the target repo
4. Fill in `PROJECT-PROFILE.md` and `WORKING-CONTEXT.md`
5. Run work through the defined agent workflow

## Core principles

1. Plan before action
2. No hidden assumptions
3. Small, reversible changes
4. Reuse before rebuild
5. Security by default
6. Test before handoff
7. Log meaningful changes
8. Keep backlog separate from in-scope work
9. Keep handoffs explicit
10. Prefer simple, maintainable solutions

## Suggested adoption flow

### For a new project

- copy the project template
- apply a preset
- choose an operating mode
- update the project profile
- start with the first story using the planner role

### For an existing project

- add the project template files
- map the current architecture and constraints
- decide the minimum sensible operating mode
- introduce the workflow gradually rather than all at once

## Versioning

This framework should be versioned like software.

- update `VERSION.md` when behaviour or structure changes
- tag meaningful versions
- keep framework changes reviewable and documented

## Source of truth rule

If a project discovers an improvement to the framework, that improvement should be fed back into this repository rather than left as local drift.
