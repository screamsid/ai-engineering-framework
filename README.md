# AI Engineering Framework

A reusable operating model and runtime governance framework for AI-assisted and multi-agent software delivery.

This repository is the source of truth for how projects should be:

- planned
- built
- reviewed
- secured
- validated
- governed
- calibrated
- improved over time

when using AI agents in engineering workflows.

Current framework version:
- v0.3.2

## Current Runtime Status

The framework now includes a working prototype runtime orchestration layer.

Implemented runtime capabilities include:

- runtime task entry pipeline
- runtime call generation
- role loading
- skill loading
- runtime routing
- confidence gates
- runtime validation
- calibration persistence
- context compilation
- memory relevance loading
- token estimation
- execution telemetry events
- adapter abstraction layer
- mock adapter execution lifecycle
- structured runtime output formatting

The framework also includes conceptual future-state governance documents.

These planned capabilities are clearly marked and are not yet implemented runtime controls.

Examples:
- `framework/CONFIDENCE-TELEMETRY.md`
- `framework/DOMAIN-TRUST-PROFILING.md`

## What This Has Evolved Into

This repository started as a reusable AI engineering workflow framework.

It is now evolving into:

- an operational governance layer for AI agents
- a runtime enforcement architecture
- a confidence-gated autonomy framework
- an institutional learning system
- a bounded adaptive orchestration model

The goal is not just:

"help AI write code"

The goal is:

"operate AI-assisted engineering systems safely, consistently, and sustainably over long periods without operational degradation."

## Why This Exists

Without structure, AI-assisted delivery tends to:

- forget rules during execution
- drift from agreed standards
- hide uncertainty
- overestimate confidence
- skip validation
- lose useful lessons between sessions
- repeat the same mistakes
- create weak handoffs
- mix planning, implementation, and review into one pass

This framework exists to reduce that.

It moves stable operational governance out of temporary chat context and into:

- reusable framework memory
- structured runtime controls
- machine-readable rule cards
- confidence gates
- skill packs
- validation schemas
- calibration loops
- telemetry concepts

## Core Principles

### Confidence controls autonomy
Agents should act autonomously only when confidence is high enough for the operational risk.

### Human validation is calibration data
Human approval and correction improve future agent behaviour.

### Governance should be lightweight
The framework must improve delivery quality without becoming bureaucratic.

### Memory must be safe and reusable
Framework memory stores abstracted operational lessons, not secrets or sensitive project detail.

### Runtime enforcement beats static instructions
Agents should not rely on remembering massive prompts.

The harness should inject minimal relevant rules and validate outputs automatically.

### Calibration matters more than raw confidence
Confidence should improve through real outcomes, validation, and human review.

## Framework Architecture

The framework is split into layered operational systems.

### Framework Layer
Human-readable governance and standards.

Examples:
- engineering standards
- security standards
- testing standards
- confidence gates
- memory lifecycle
- adherence controls

### Runtime Layer
Machine-readable operational enforcement.

Examples:
- runtime runner
- rule cards
- invocation schemas
- validators
- adapters
- runtime loaders
- confidence thresholds
- escalation rules
- telemetry events

### Skills Layer
Reusable operational execution packs.

Examples:
- secure coding
- smoke testing
- validation testing
- security review
- dependency analysis

### Memory Layer
Durable institutional learning.

Examples:
- reusable lessons
- anti-patterns
- calibration improvements
- validation improvements
- drift prevention patterns

### Telemetry Layer
Operational measurement and calibration.

Examples:
- confidence calibration
- adherence scoring
- escalation frequency
- rollback tracking
- memory usefulness

## Runtime Execution Lifecycle

Current runtime execution flow:

```text
HUMAN-TASK-ENTRY.md
  ↓
RuntimeCallBuilder
  ↓
RUNTIME-CALL.yaml
  ↓
RuntimeRunner
  ↓
Router selects role + adapter
  ↓
Role + skills loaded
  ↓
Relevant memory loaded
  ↓
Context assembled
  ↓
Context compiled
  ↓
Token estimate calculated
  ↓
Adapter invoked
  ↓
Output validated
  ↓
Confidence calibrated
  ↓
Telemetry event emitted
  ↓
Human-readable output generated
```

## Confidence-Gated Autonomy

The framework uses confidence gates to control autonomy.

Example:

| Confidence | Behaviour |
| --- | --- |
| 90-100% | Autonomous execution allowed |
| 75-89% | Low-risk autonomous execution only |
| 50-74% | Human validation required |
| 0-49% | Stop and escalate |

Confidence is adjusted by:

- risk level
- validation outcomes
- calibration policy
- runtime governance rules

Domain trust profiling is currently conceptual and not implemented runtime behaviour.

## Multi-Vendor Design

The framework is intentionally vendor-agnostic.

Current adapter structure includes:

- mock adapter
- Codex scaffold
- Claude Code scaffold
- Antigravity scaffold

Roles map to capability tiers rather than hardcoded model names.

## Repository Structure

```text
.
├── README.md
├── VERSION.md
├── framework/
│   ├── AGENT-ADHERENCE.md
│   ├── CONFIDENCE-CALIBRATION.md
│   ├── CONFIDENCE-GATES.md
│   ├── CONFIDENCE-RATINGS.md
│   ├── CONFIDENCE-TELEMETRY.md
│   ├── CONTEXT-MANAGEMENT.md
│   ├── DOMAIN-TRUST-PROFILING.md
│   ├── DRIFT-CONTROL.md
│   ├── FRAMEWORK-MEMORY.md
│   ├── FRAMEWORK-ROADMAP.md
│   ├── FRICTION-CONTROL.md
│   ├── HARNESS-INTEGRATION.md
│   ├── MEMORY-FEEDBACK-LOOP.md
│   ├── MEMORY-LIFECYCLE.md
│   ├── RISK-CLASSIFICATION.md
│   ├── SKILLS.md
│   ├── STRUCTURED-RULES.md
│   ├── TESTING-STANDARDS.md
│   └── WORKFLOW.md
├── runtime/
│   ├── README.md
│   ├── version.py
│   ├── runner.py
│   ├── entry/
│   ├── adapters/
│   ├── audit/
│   ├── calibration/
│   ├── compiler/
│   ├── formatters/
│   ├── gates/
│   ├── invocation/
│   ├── loaders/
│   ├── memory/
│   ├── output/
│   ├── router/
│   ├── rules/
│   ├── telemetry/
│   ├── tokens/
│   └── validators/
├── examples/
│   ├── python-automation/
│   └── runtime-invocation/
├── skills/
│   ├── secure-coding/
│   ├── smoke-testing/
│   └── validation-testing/
├── presets/
│   ├── infra-automation/
│   └── security-tool/
└── tests/
```

## Current Prototype Boundaries

The current runtime implementation intentionally includes prototype-stage constraints.

Examples:
- embedded seed memory
- mock adapter default execution
- conceptual telemetry analytics
- conceptual domain trust profiling
- no persistent long-term runtime datastore

These boundaries are intentional to keep the runtime:

- lightweight
- testable
- low-blast-radius
- operationally understandable

## Current Direction

Current priorities:

- expand runtime orchestration
- improve adapter execution paths
- expand role cards
- expand skill packs
- improve calibration persistence
- improve runtime validation depth
- build framework compliance automation
- add future memory provider abstraction
- add safer runtime persistence models

## Final Note

This framework should help AI-assisted engineering become:

- safer
- more consistent
- more explainable
- more governable
- more scalable
- less dependent on fragile chat context

If the framework becomes:

- bloated
- overly rigid
- bureaucratic
- harder to use than the problem it solves

then simplify it.

The goal is bounded adaptive autonomy, not process theatre.
