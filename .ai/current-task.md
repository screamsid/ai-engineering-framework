# Current Task

## Task

Refactor bootstrap into a deterministic orchestration layer driven by framework and project profiles.

## Working Mode

Current mode: maintenance

## Outcome Required

Bootstrap validates and resolves profiles, loads declared skills and memory, writes deterministic bootstrap state, and delegates engineering behaviour to skills.

## Scope

### In scope

- Bootstrap skill refactor
- Bootstrap validation skill
- Framework profile definitions
- Project profile template migration
- Bootstrap report and project health state files
- Documentation and template updates

### Out of scope

- Runtime execution engine rewrite
- Product-specific skills
- Cloudflare collector implementation

## Validation Plan

- Confirm bootstrap uses profile-driven skill loading.
- Confirm Bootstrap delegates rather than implements planning, review, testing, Git, memory, workspace, and promotion.
- Confirm templates use `.ai/profiles/project-engineer.yaml`.
- Review Git diff before completion.
- Update task ledger.
- Update project memory only with validated reusable learning.

## Confidence Gate

Stop and ask for review if confidence drops below 90% or if implementation requires runtime behaviour that cannot be inspected.
