# Reviewing Skill

## Purpose

Close the engineering feedback loop by checking whether the task outcome was met safely and cleanly.

Review is mandatory before completion.

## Required Inputs

- task outcome
- working mode
- files changed
- diff summary
- validation results
- project profile
- relevant memory
- confidence gates

## Required Behaviour

1. Confirm the requested outcome was met.
2. Confirm changes stayed inside scope.
3. Confirm working mode rules were followed.
4. Confirm no unrelated refactors were introduced.
5. Confirm no protected information or raw generated output was added.
6. Confirm validation was run or explain why it could not be run.
7. Identify any remaining risks.
8. Produce a confidence rating.
9. Identify memory candidates.
10. Update the task ledger.

## Required Outputs

- review_summary
- scope_check
- validation_summary
- risk_summary
- confidence_rating
- memory_candidates
- task_ledger_update
- next_task

## Stop Conditions

Do not mark the task complete when:

- outcome is only partially met
- files changed outside scope without explanation
- validation failed
- validation was skipped without reason
- confidence is below the completion gate
- protected information may have been added
- task ledger was not updated

## Confidence Guidance

Raise confidence when:

- tests passed
- diff is small and focused
- project profile was followed
- memory and task ledger are updated

Lower confidence when:

- validation is manual only
- external behaviours were assumed
- review found unrelated changes
- project rules were unclear

## Candidate Lessons

Propose memory updates when:

- a validated implementation pattern should be reused
- a repeated mistake was found
- a project rule needs clarification
- a confidence gate needs adjustment
