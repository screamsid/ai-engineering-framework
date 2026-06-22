# Project Memory

Project memory is curated, validated, reusable knowledge for this repository.

It is not a scratchpad. It must not contain secrets, raw outputs, customer data, generated artefacts, or unverified assumptions.

## Architecture Decisions

### ADR-001 - Bootstrap orchestrates, skills perform

**Status:** accepted

**Date:** 2026-06-22

**Confidence:** 91%

**Validated by:** framework refactor and documentation review

**Decision:**

Bootstrap is a deterministic orchestration layer. It validates and resolves declared configuration, loads profiles, loads skills, loads memory, writes bootstrap state, and stops or reports ready. Engineering behaviour belongs in skills. Profiles compose skills. Projects configure profiles.

**Reason:**

The previous bootstrap model mixed orchestration with planning, review, Git, memory, workspace, and promotion responsibilities. Separating these concerns keeps the framework reusable, technology agnostic, and easier for projects to adopt.

**Impact:**

Future framework work should extend existing skills before adding bootstrap behaviour. New project-specific behaviour must live in project profiles or project skills, not in bootstrap.

## Project Conventions

- Framework profiles live under `framework/profiles/<profile-name>/profile.yaml`.
- Project profiles live under `.ai/profiles/<profile-name>.yaml`.
- Bootstrap references project profiles by name using `agent.profile`.
- Bootstrap reports state through `.ai/bootstrap-report.md` and `.ai/project-health.yaml`.

## Known Pitfalls

- Do not reintroduce planning, review, testing, Git, memory, workspace, or promotion behaviour directly into bootstrap.
