---
name: harness-integration
description: Standards for integrating the framework into agent harnesses so rules can be called, injected, validated, and enforced.
---
# Harness Integration

The framework must be callable by agent harnesses.

A harness may be:

- Codex
- Claude Code
- Cursor
- Gemini
- a custom orchestrator
- CI/CD automation
- a local agent runner
- a multi-agent control plane

The goal is to move from static documentation to operational enforcement.

## Core Principle

Do not rely on agents remembering the whole framework.

The harness should inject the smallest relevant rule set at the right time, then validate the agent output against those rules.

## Harness Responsibilities

A framework-aware harness should:

1. identify the current task type
2. identify the active role
3. load the relevant rule card
4. load relevant skill packs
5. load relevant memory only when useful
6. inject concise rules into the agent context
7. validate required outputs
8. apply confidence gates
9. record calibration data
10. propose memory updates when lessons are found

## Invocation Flow

```text
Task arrives
  ↓
Classify task and risk
  ↓
Select agent role
  ↓
Load role card
  ↓
Load relevant skill packs
  ↓
Load relevant memory
  ↓
Inject concise framework context
  ↓
Agent works
  ↓
Validate output structure
  ↓
Apply confidence gate
  ↓
Human validation if required
  ↓
Record outcome and calibration
  ↓
Propose memory updates
```

## Minimal Framework Call

Every agent task should start with a minimal framework call.

Example:

```yaml
framework_call:
  task: "Implement feature X"
  role: "builder"
  risk: "medium"
  required_rules:
    - core-rules
    - agent-adherence
    - confidence-gates
    - testing-standards
  required_skills:
    - secure-coding
    - smoke-testing
  required_outputs:
    - implementation_summary
    - validation_summary
    - confidence_gate
    - known_gaps
    - handoff
```

## Rule Injection Strategy

Avoid injecting the full framework.

Inject:

- role card
- relevant stop conditions
- required outputs
- confidence gate threshold
- relevant skill checklist
- relevant memory items

Do not inject:

- unrelated roles
- unrelated skills
- stale context
- full documentation unless needed

## Output Validation

The harness should validate that required sections exist.

Examples:

- missing confidence gate: fail or request correction
- missing validation summary: fail or request correction
- missing known gaps: request correction
- missing security review for high-risk work: block
- confidence below threshold without human validation: block

## Human Validation Integration

When confidence gates require human validation, the harness must:

- pause execution
- present the decision clearly
- capture the human response
- continue only after approval or correction
- record the outcome for calibration

## Memory Integration

After work completes, the harness should ask:

- was a reusable lesson found?
- is it project-local or framework-wide?
- is it sanitised?
- what confidence applies?
- should the Memory Reviewer inspect it?

## Non-Hindrance Rule

Harness integration should improve reliability without turning every task into a slow workflow.

Start by enforcing only high-value controls:

- confidence required
- risk classification required
- validation required
- known gaps required
- human validation when confidence is below threshold
- human validation for critical risk

## Completion Rule

Harness integration is successful when agents can call the framework repeatedly with low friction and the system catches missing validation, hidden uncertainty, and unsafe autonomy before handoff.
