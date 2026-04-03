# AI Engineering Team

This directory defines the operating model for the engineering agent team.

## Team roles

- Planner
  - reviews stories
  - identifies gaps, risks, dependencies, and constraints
  - produces an executable plan

- Builder
  - implements approved work in small steps
  - keeps changes minimal and traceable
  - updates relevant docs and the audit log

- Reviewer
  - checks correctness, maintainability, scope control, and acceptance criteria

- Security Reviewer
  - checks security risks, dependency choices, secret handling, validation, and attack surface

- Git Manager
  - checks branch discipline, commit hygiene, tagging, and rollback readiness

- Release Manager
  - confirms release or merge readiness and checks the definition of done

## Non-negotiables

- No coding before planning
- No silent assumptions on unclear requirements
- No large unstructured commits
- No bypassing security or testing requirements
- No mixing backlog ideas into in-scope work without explicit reprioritisation
- No incomplete handoff

## Operating order

1. planner
2. builder
3. reviewer
4. security reviewer where required
5. git manager
6. release manager
