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

## Start Here

If this is your first time using the framework:

➡️ Read: `docs/QUICKSTART.md`

The quickstart gets you from:

- clean clone
- to a successful runtime execution
- in under 10 minutes

using the real runtime runner and adapter lifecycle.

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
- adapter abstraction layer
- mock adapter execution lifecycle
- Codex CLI adapter implementation
- governance-aware adapter execution constraints
- structured runtime output formatting

Partially implemented runtime capabilities include:

- pre-execution token estimation
- partial execution telemetry event generation

Planned or future-state capabilities include:

- post-execution actual token capture
- token cost calculation and tracking
- telemetry analytics pipeline
- domain trust profiling
- confidence telemetry analytics

The framework also includes conceptual future-state governance documents.

These planned capabilities are clearly marked and are not yet implemented runtime controls.

Examples:
- `framework/CONFIDENCE-TELEMETRY.md`
- `framework/DOMAIN-TRUST-PROFILING.md`

## Token and Cost Visibility

The current runtime includes lightweight pre-execution token estimation.

Current behaviour:

- payload size is estimated before adapter invocation
- the estimate is included in runtime telemetry events
- estimates are generated using a rough approximation model
- the current approximation is based on character count divided by four

This estimator exists to provide:

- basic payload visibility
- oversized-context warnings
- early governance instrumentation

It is intentionally lightweight during the prototype stage.

Current limitations:

- estimates are approximate only
- no provider-specific tokenisation exists yet
- estimates are not calibrated against real token usage
- no adaptive estimation improvement exists yet
- post-execution actual token capture is not implemented yet
- token cost calculation is not implemented yet
- telemetry aggregation and analytics are not implemented yet

Token cost tracking and actual token reconciliation are planned future capabilities.

Planned follow-on work:
- STORY-TOKEN-COST-TRACKING

The goal is progressive observability maturity without prematurely introducing heavy telemetry infrastructure into the prototype runtime.

## Adapter Status

| Adapter | Status | Notes |
| --- | --- | --- |
| Mock | Stable prototype | Safe default execution path |
| Codex | Implemented, tested-with-mocks, unvalidated | Real subprocess-backed CLI execution |
| Claude Code | Scaffold only | Future story |
| Antigravity | Scaffold only | Future story |

The Codex adapter currently:

- invokes the local Codex CLI
- enforces governance execution constraints
- supports timeout handling
- supports approval-mode mapping
- supports structured adapter result normalisation
- is tested using mocked subprocess execution

The Codex adapter has not yet completed real-task validation runs against a live Codex CLI.

Until validated:
- the mock adapter remains the safest default
- Codex should be treated as prototype-stage runtime execution

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

## Runtime Governance Enforcement

The runtime now actively influences execution behaviour.

Examples:

- filesystem write restrictions can downgrade execution mode
- high-risk tasks can prevent autonomous execution
- human validation requirements create explicit execution checkpoints
- adapter execution settings are governed centrally through runtime policy

This is an intentional architectural direction.

The framework is designed so governance becomes executable runtime behaviour, not just prompt guidance.

## Framework Architecture

The framework is split into layered operational systems.

### Framework Layer
Human-readable governance and standards.

### Runtime Layer
Machine-readable operational enforcement.

### Skills Layer
Reusable operational execution packs.

### Memory Layer
Durable institutional learning.

### Telemetry Layer
Operational measurement and calibration.

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
Governance execution constraints applied
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

## Multi-Vendor Design

The framework is intentionally vendor-agnostic.

Current adapter structure includes:

- mock adapter
- Codex CLI adapter
- Claude Code scaffold
- Antigravity scaffold

Roles map to capability tiers rather than hardcoded model names.

## Current Prototype Boundaries

The current runtime implementation intentionally includes prototype-stage constraints.

Examples:
- mock adapter remains default execution path
- Codex adapter not yet operationally validated against real workloads
- embedded seed memory
- approximate token estimation only
- no post-execution actual token capture
- no token cost calculation
- no telemetry aggregation backend
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

- validate Codex adapter against real non-destructive tasks
- improve token visibility and telemetry maturity
- implement token cost tracking
- implement post-execution token reconciliation
- expand adapter execution paths
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
