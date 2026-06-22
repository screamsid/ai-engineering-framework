# Promotion Skill

## Purpose

Move work deliberately from research or experimentation into production-quality project artefacts.

Promotion prevents temporary work from becoming production code by accident.

## Required Inputs

- working mode
- task outcome
- prototype or sandbox output
- validation evidence
- review summary
- project profile
- workspace rules
- confidence gates

## Required Behaviour

1. Identify the current source mode.
2. Identify the target mode.
3. Confirm promotion is explicitly requested or approved.
4. Review the artefact being promoted.
5. Remove temporary assumptions and debug-only code.
6. Add tests or validation appropriate to the target mode.
7. Move only the minimum required artefacts into production paths.
8. Update documentation when needed.
9. Update project memory only with validated learning.
10. Update the task ledger with the promotion decision.

## Promotion Path

```text
Research
  ↓
Sandbox
  ↓
Prototype
  ↓
Production
```

Skipping stages requires explicit human approval.

## Required Outputs

- promotion_source
- promotion_target
- promoted_files
- discarded_files
- validation_summary
- review_summary
- confidence_rating
- memory_updates
- task_ledger_update

## Stop Conditions

Do not promote when:

- promotion was not requested or approved
- validation evidence is missing
- confidence is below the target mode gate
- temporary debug logic remains
- generated output would be committed unintentionally
- project profile rules are not met

## Confidence Guidance

Raise confidence when:

- the promoted work is small and reviewed
- automated tests passed
- temporary files were cleaned up
- documentation reflects the change

Lower confidence when:

- the work came from a loose experiment
- assumptions remain unverified
- validation is manual only
- target production behaviour is unclear

## Candidate Lessons

Propose memory updates when:

- a successful promotion pattern should be reused
- a failed promotion exposed a project rule gap
- a sandbox constraint needs adjustment
- validation requirements need tightening
