# Core Rules

These rules apply to all roles, all stories, and all projects using this framework.

They are non-negotiable unless explicitly overridden in a project profile.

## 1. Plan before action
No code, configuration, or file changes should be made until the task is understood and a plan exists.

A quick plan is acceptable.  
No plan is not acceptable.

## 2. No hidden assumptions
Do not silently fill gaps in requirements, scope, architecture, or intent.

If something is unclear:
- identify the gap
- state the likely interpretation if needed
- state the risk of proceeding

## 3. Work in small, safe steps
Changes must be:
- small
- reviewable
- reversible

Avoid large, mixed, or difficult-to-rollback changes.

## 4. Keep scope tight
Only implement what is required for the current story.

Do not include:
- opportunistic refactors
- unrelated fixes
- new ideas discovered during implementation

## 5. New ideas go to the backlog
Any improvement, idea, or discovery outside scope must be:
- recorded in the backlog
- not silently included in the current work

## 6. Reuse before rebuild
Before creating new code or structure, check for:
- existing modules
- shared utilities
- established patterns
- documented approaches

Do not rebuild something that already exists without reason.

## 7. Security is mandatory
All work must consider:
- least privilege
- safe handling of secrets
- input validation
- dependency risk
- logging safety
- data exposure

Security is not optional where risk exists.

## 8. Validation is mandatory
Every meaningful change must be validated.

At minimum:
- smoke testing is required

Where risk is higher:
- deeper testing is required

## 9. Audit all meaningful changes
Every meaningful change must be recorded in the audit log.

Include:
- what changed
- why it changed
- files affected
- risks considered
- validation performed

## 10. Git discipline is required
All changes must follow git standards:

- small commits
- clear commit messages explaining why
- one logical change per commit where possible
- no large “catch-all” commits

## 11. Protect rollback
All changes must be easy to:
- understand
- isolate
- revert

If rollback would be difficult, the change is too large or unclear.

## 12. Handoffs must be explicit
When handing work over, include:

- current state
- what changed
- what was validated
- known risks
- what remains
- next recommended step

Do not rely on implied understanding.

## 13. Update working context
Where relevant, update working context so future work does not need to reconstruct state.

## 14. Surface risk early
If a path introduces material risk:
- call it out immediately
- do not bury it
- do not proceed silently

## 15. Simplicity over cleverness
Prefer solutions that are:
- clear
- maintainable
- predictable

Avoid unnecessary complexity.

## 16. Do not proceed on unclear stories
Before starting, the story must be reviewed.

If the story:
- lacks clarity
- is missing acceptance criteria
- has undefined scope

Then:
- identify the gaps
- do not proceed blindly

## 17. Separate responsibilities
Planning, implementation, review, and validation should not collapse into a single step.

Respect role boundaries.

## 18. Completion means fully complete
A story is not complete until:

- requirements are met
- validation is complete
- audit log is updated
- review is complete
- security review is complete where required

Partial completion is not completion.

## 19. No silent behaviour changes
All meaningful changes must be:
- visible
- traceable
- explained

Hidden behaviour changes are not acceptable.

## 20. The framework must be followed
These rules exist to:

- reduce inconsistency
- improve quality
- reduce risk
- improve reuse

If they are ignored, the system degrades quickly.