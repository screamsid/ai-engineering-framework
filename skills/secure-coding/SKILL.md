# Secure Coding Skill

## Purpose

Provide reusable secure coding guidance for implementation tasks.

The goal is to:

- reduce security regressions
- standardise secure behaviour
- reduce repeated mistakes
- improve validation quality

## Core Checks

- input validation
- output encoding
- secret handling
- least privilege
- dependency review
- subprocess safety
- logging safety
- unsafe deserialisation
- injection risks
- authentication handling
- authorisation boundaries

## Required Outputs

- implementation_summary
- security_considerations
- validation_summary
- confidence_gate
- known_gaps

## Required Validation

- smoke testing
- security review for high-risk work
- validation of security-sensitive paths

## Stop Conditions

- unresolved security risk
- unclear trust boundary
- unvalidated external input handling
- insecure secret exposure

## Confidence Guidance

Lower confidence when:

- security-sensitive logic was not validated
- assumptions exist around trust boundaries
- dependencies were not reviewed
- security validation could not be completed

## Candidate Lessons

This skill should propose memory candidates when:

- a new security anti-pattern is found
- a reusable secure pattern is identified
- validation exposed a recurring weakness
- a human correction improved security posture
