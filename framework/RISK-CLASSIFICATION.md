---
name: risk-classification
description: Risk classification standards for confidence gates, autonomy, validation, and escalation.
---
# Risk Classification

Risk classification determines:

- required validation
- confidence thresholds
- autonomy limits
- escalation requirements
- reviewer involvement

## Core Principle

Confidence alone is not enough.

The same confidence score may be acceptable for low-risk work but unsafe for high-risk work.

## Risk Levels

| Level | Meaning |
| --- | --- |
| Low | Limited operational impact and easy rollback |
| Medium | Moderate operational or security impact |
| High | Significant operational, security, or customer impact |
| Critical | Severe impact, irreversible damage, or major security risk |

## Low Risk Examples

- documentation updates
- formatting changes
- non-production scripts
- isolated test changes
- internal reporting updates

## Medium Risk Examples

- logic changes
- parser updates
- CI/CD changes
- dependency updates
- integration changes
- non-critical automation

## High Risk Examples

- production infrastructure changes
- authentication changes
- firewall or security policy changes
- privilege handling changes
- architecture changes
- data processing changes

## Critical Risk Examples

- destructive operations
- credential rotation mistakes
- customer-impacting security changes
- irreversible migrations
- large-scale production modifications
- memory promotion involving sensitive source material

## Required Behaviour By Risk

| Risk | Minimum Validation | Human Review |
| --- | --- | --- |
| Low | Smoke test | Optional |
| Medium | Functional validation | Recommended |
| High | Security and validation review | Required |
| Critical | Multi-review plus approval | Mandatory |

## Confidence Thresholds

| Risk | Minimum Autonomous Confidence |
| --- | --- |
| Low | 85% |
| Medium | 90% |
| High | 95% |
| Critical | Human approval always required |

## Escalation Rules

Escalate when:

- confidence is below threshold
- rollback is unclear
- validation is incomplete
- security impact is uncertain
- reviewers disagree materially
- operational blast radius is large

## Completion Rule

Risk classification is successful when:

- low-risk work remains fast
- high-risk work remains controlled
- escalation is proportional
- governance improves safety without excessive friction
