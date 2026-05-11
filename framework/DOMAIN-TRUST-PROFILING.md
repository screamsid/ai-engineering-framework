---
name: domain-trust-profiling
description: Standards for measuring and weighting agent trustworthiness by domain and task type.
---
# Domain Trust Profiling

Agents are not equally reliable across all domains.

The framework should learn where agents are:

- highly reliable
- moderately reliable
- weak
- overconfident
- underconfident

## Core Principle

Trust should be domain-specific, not global.

An agent may perform strongly in:

- smoke testing
- structured parsing
- documentation generation

While performing poorly in:

- security review
- architecture reasoning
- edge-case analysis

## Domain Profiles

Example domains:

- smoke testing
- secure coding
- dependency analysis
- security review
- architecture review
- infrastructure automation
- parsing
- release readiness
- memory review
- drift analysis

## Trust Signals

Useful trust signals include:

- validation success rate
- human approval rate
- rollback rate
- incident rate
- reviewer disagreement
- false positive rate
- false negative rate
- confidence calibration quality
- adherence score

## Example Profile

```markdown
## Domain Trust Profile

Domain: Smoke Testing
Historical Accuracy: 96%
Human Correction Rate: 3%
Confidence Calibration: Strong
Adherence Score: 94%
Recommended Autonomy: High

Domain: Security Review
Historical Accuracy: 72%
Human Correction Rate: 24%
Confidence Calibration: Medium
Adherence Score: 83%
Recommended Autonomy: Medium with mandatory reviewer involvement
```

## Behavioural Use

Trust profiles may influence:

- confidence weighting
- autonomy thresholds
- reviewer requirements
- escalation behaviour
- required validation depth

## Anti-Pattern

Do not assume:

- a generally capable model is reliable in every domain
- high confidence always means high accuracy
- past success in one area transfers automatically to another

## Completion Rule

Trust profiling is successful when:

- autonomy increases safely in strong domains
- human oversight increases in weak domains
- confidence becomes more realistic over time
