# Core Rules

These rules apply to every role and every task.

## 1. Plan before action
No code or file changes may be made until the work has been understood and a plan has been produced.

## 2. No assumptions
If requirements, scope, or intent are unclear, the gap must be stated explicitly.
Where possible, propose the most likely interpretation and explain the risk.

## 3. Small safe steps
Work in small, reversible increments.
Prefer several focused changes over one large mixed change.

## 4. Reuse before rebuild
Check existing code, modules, scripts, and documentation before creating something new.

## 5. Keep changes minimal
Change only what is necessary to complete the story safely.

## 6. Security by default
Follow secure coding principles, least privilege, safe secret handling, and dependency awareness.

## 7. Test before handoff
Every implementation change must be validated with smoke tests at a minimum.

## 8. Log what changed
Every meaningful change must update the audit log with the story reference, files changed, summary, risks, and validation performed.

## 9. Backlog discipline
Ideas discovered during execution must be added to the backlog rather than merged into the current story unless explicitly in scope.

## 10. Handoff clarity
Every handoff must include the current state, what changed, validation status, known risks, and the recommended next step.

## 11. Simplicity wins
Prefer readable, maintainable, boring solutions over clever ones.

## 12. Stop on unsafe changes
If the requested path creates material security, stability, compliance, or data-loss risk, stop and flag it clearly.
