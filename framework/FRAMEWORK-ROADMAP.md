---
name: framework-roadmap
description: Structured roadmap for future framework evolution.
---
# Framework Roadmap

This roadmap tracks important future framework evolution work.

The purpose is to:

- avoid losing strategic ideas in conversation history
- prioritise future framework improvements
- maintain continuity across sessions
- prevent repeated rediscovery of the same needs

## Priority Levels

| Priority | Meaning |
| --- | --- |
| P0 | Critical foundation capability |
| P1 | Strongly recommended near-term improvement |
| P2 | Important medium-term evolution |
| P3 | Experimental or future exploration |

---

# P0: Critical Foundation

## Automated Secret Scanning Before Memory Promotion

Status: Planned

Purpose:
- prevent sensitive data leakage into framework memory

Ideas:
- integrate secret scanning before promotion approval
- block memory promotion on detected secrets
- add sanitisation workflow

---

## Skill Pack Directory

Status: Planned

Purpose:
- create reusable operational skill packs

Initial Packs:
- secure coding
- smoke testing
- validation testing
- security review
- architecture review
- git hygiene
- release readiness
- dependency analysis

---

## Framework Memory Index

Status: Planned

Purpose:
- provide structured discoverability of framework memory
- avoid duplicate lessons
- support memory lifecycle tracking

---

# P1: Near-Term Improvements

## Memory Scoring

Status: Planned

Purpose:
- score usefulness and trustworthiness of memories

Potential Signals:
- confidence
- reuse frequency
- validation success
- reviewer agreement
- friction introduced

---

## Memory Harm Detection

Status: Planned

Purpose:
- identify memories causing operational drag or poor behaviour

Examples:
- over-restrictive guidance
- obsolete warnings
- high false-positive patterns
- delivery slowdown without risk reduction

---

## Agent Disagreement Resolution

Status: Planned

Purpose:
- handle conflicting conclusions between agents or reviewers

Potential Features:
- confidence comparison
- escalation paths
- evidence weighting
- reviewer arbitration

---

## Adversarial Review Skill

Status: Planned

Purpose:
- intentionally challenge assumptions and outputs

Examples:
- attack-path analysis
- edge-case probing
- validation gap hunting
- rollback failure simulation

---

# P2: Medium-Term Evolution

## Framework Compliance Automation

Status: Planned

Purpose:
- automate adherence checking inside CI/CD or harnessing systems

Examples:
- missing confidence detection
- missing validation detection
- scope drift checks
- audit completeness checks

---

## Memory Telemetry

Status: Planned

Purpose:
- measure whether memory is helping or harming

Potential Metrics:
- reuse rate
- adherence impact
- friction score
- stale memory detection
- ignored guidance frequency

---

## Confidence Calibration

Status: Planned

Purpose:
- improve reliability of confidence scoring

Examples:
- compare confidence versus real outcomes
- detect overconfidence trends
- detect underconfidence trends

---

# P3: Experimental Exploration

## Multi-Agent Reflection Loops

Status: Exploratory

Purpose:
- allow agents to collaboratively review and improve workflows

Risk:
- runaway complexity
- excessive review loops
- hallucinated consensus

---

## Adaptive Rule Injection

Status: Exploratory

Purpose:
- dynamically inject the smallest relevant rule set for the task

Potential Benefits:
- reduced context usage
- improved adherence
- reduced prompt bloat

---

## Behavioural Drift Analytics

Status: Exploratory

Purpose:
- identify recurring agent behavioural patterns over time

Examples:
- repeated scope expansion
- recurring validation gaps
- recurring hidden assumptions
- confidence inflation

---

# Roadmap Rule

The roadmap is guidance, not a mandatory delivery sequence.

Framework evolution should remain:

- pragmatic
- lightweight
- evidence-driven
- operationally useful

Do not add complexity without clear value.
