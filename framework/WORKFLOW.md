# Workflow

## Standard story flow

1. Story intake
2. Story review
3. Clarification and risk identification
4. Planning
5. Implementation
6. Local validation
7. Review
8. Security review where needed
9. Git and release checks
10. Completion or return for rework

## Detailed flow

### 1. Story intake
Planner reads the story and confirms:
- objective
- scope
- acceptance criteria
- dependencies
- constraints

### 2. Story review
Planner checks whether the story is actionable.
If it is not, the planner records the missing details.

### 3. Clarification and risk identification
Planner identifies:
- ambiguous requirements
- architectural risks
- security concerns
- testing needs
- rollback concerns

### 4. Planning
Planner produces:
- implementation steps
- file impact summary
- validation plan
- rollback considerations
- backlog items discovered

### 5. Implementation
Builder:
- works in small steps
- updates docs where needed
- updates the audit log
- does not expand scope without instruction

### 6. Local validation
Builder runs smoke tests and any relevant checks.

### 7. Review
Reviewer checks:
- acceptance criteria
- code quality
- maintainability
- scope discipline
- regression risk

### 8. Security review
Security Reviewer checks:
- input validation
- auth and access boundaries
- secrets handling
- insecure dependencies
- logging safety
- injection paths
- dangerous defaults

### 9. Git and release checks
Git Manager confirms:
- branch naming
- commit quality
- change grouping
- rollback readiness
- tags where appropriate

Release Manager confirms:
- docs updated
- audit log updated
- definition of done met

### 10. Completion
A story is only complete when all mandatory checks pass.

## Loopback rule
If review or security review fails, the work returns to Builder with explicit findings.
