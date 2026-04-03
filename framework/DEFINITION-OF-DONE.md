---
name: definition-of-done
description: A story is only complete when all required conditions are satisfied.
---
# Definition of Done

A story is only complete when all required conditions are satisfied.

“Mostly done” is not done.

---

## Mandatory Conditions

All of the following must be true:

### 1. Requirements met
- the story objective is achieved
- acceptance criteria are satisfied
- scope has been respected

---

### 2. Implementation quality
- changes are readable and maintainable
- no unnecessary complexity
- no hidden behaviour
- no unrelated changes included

---

### 3. Validation complete
- smoke tests completed (minimum)
- deeper testing completed where required
- results clearly recorded
- known gaps explicitly stated

---

### 4. Review complete
- reviewer has assessed the work
- findings have been addressed
- no unresolved critical issues remain

---

### 5. Security review complete (when required)
Required if the change affects:

- authentication or authorisation
- secrets or credentials
- external inputs
- file handling
- subprocess execution
- dependencies
- APIs or integrations
- sensitive data

Security concerns must be:
- addressed
- or explicitly recorded as residual risk

---

### 6. Audit log updated
Audit entry must include:

- what changed
- why it changed
- files affected
- risks considered
- validation performed
- follow-up required
- commit reference (if available)

---

### 7. Git standards met
- commits are small and logical
- commit messages explain why
- no unrelated changes bundled
- history is readable and traceable
- rollback is practical

---

### 8. Backlog discipline maintained
- out-of-scope ideas recorded in backlog
- no silent scope expansion

---

### 9. Working context updated (when relevant)
- current state is recorded
- next steps are clear
- key changes are captured

---

### 10. Handoff is clear
If work is handed off, it must include:

- current state
- what changed
- validation status
- known risks
- remaining work
- recommended next step

---

## Not Done If

A story is not complete if any of the following apply:

- requirements are partially met
- validation is missing or unclear
- review has not been completed
- security-sensitive changes are unreviewed
- audit log is missing
- git history is unclear or messy
- scope has drifted without control
- known risks are hidden
- work cannot be easily understood or reviewed

---

## Working Rule

A story is only done when another engineer can:

- understand what changed
- understand why it changed
- see how it was validated
- see what risks remain
- safely build on top of it
- safely roll it back if needed

---

## Enforcement

If any mandatory condition is not met:

- the story is not complete
- the work must return for rework

Completion is a decision, not a feeling.