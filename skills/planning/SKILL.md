# Planning Skill

## Purpose

Convert a task into the smallest safe plan that achieves the required outcome.

Planning happens after bootstrap and before implementation.

## Required Inputs

- active task
- working mode
- project profile
- relevant project memory
- Git state summary
- workspace boundaries
- confidence gates

## Required Behaviour

1. Restate the required outcome.
2. Identify the current working mode.
3. Confirm in-scope and out-of-scope work.
4. Check whether existing project files already solve part of the task.
5. Choose the smallest complete change.
6. Identify files likely to change.
7. Define validation before implementation.
8. Identify risks and confidence gates.
9. Avoid speculative architecture.
10. Avoid placeholder deliverables.

## Required Outputs

- outcome_summary
- working_mode
- scope_summary
- planned_changes
- validation_plan
- risk_summary
- confidence_before_work

## Stop Conditions

Pause before implementation when:

- the outcome is unclear
- the working mode conflicts with the requested change
- required files are missing
- the task requires access that is unavailable
- the change would exceed scope
- confidence is below the project gate

## Confidence Guidance

Raise confidence when:

- project profile is complete
- relevant memory exists
- validation is available
- change surface is small

Lower confidence when:

- requirements conflict
- validation cannot be run
- project architecture is unclear
- external service behaviour is unconfirmed

## Candidate Lessons

Propose memory updates when:

- the same planning issue appears repeatedly
- a useful task decomposition pattern is validated
- a project boundary needs documenting
- an assumption is confirmed through validation
