# AI Engineering Framework

A reusable operating model and runtime governance framework for AI-assisted and multi-agent software delivery.

Current framework version:
- v0.4.0

---

# Project Overview

> ⚠️ Work in Progress / Prototype

This project is actively being built and should currently be treated as a prototype rather than a finished product.

Some areas are fully working, some are partially implemented, and some sections are intentionally skeletal. In a few places, structure and placeholders exist simply so I don’t lose the direction of where the project is going or forget functionality that still needs fleshing out later.

I’d rather be honest about that than pretend everything here is production-ready.

The broader goal behind this project is exploring the gap between fast-moving AI-assisted development and genuinely production-ready engineering.

AI can generate code quickly.

The harder problem is building the guardrails, validation, operational trust, governance, and engineering discipline needed to turn rapidly generated output into systems people can actually trust and operate safely.

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

A core architectural principle of the framework is separating:

- durable capability abstractions
from:
- fast-moving provider model identifiers

The framework intentionally treats model mappings as configurable operational state rather than hardcoded runtime truth.

That means:

- capability tiers remain stable
- provider model identifiers are expected to drift over time
- runtime operators are expected to periodically review and update model mappings as vendors release newer models

This is considered a normal operational maintenance concern, similar to dependency or infrastructure lifecycle management.

---

# Why This Exists

AI has dramatically reduced the friction involved in generating software.

What it has not reduced is the operational, cognitive, and organisational cost of trusting that software.

In many environments, humans are now becoming the bottleneck, not because they are slow, but because they remain responsible for validation, governance, operational safety, maintainability, and risk ownership.

This creates a growing disconnect between:

- Speed of generation
- Speed of understanding
- Speed of trust

The result is often:

- Review fatigue
- Cognitive overload
- Shallow validation
- Governance bypass pressure
- Reduced confidence in changes
- Increased burnout across engineering teams

This project exists to explore how we engineer that gap more safely.

Not by removing humans from the process, but by improving:

- Confidence signalling
- Validation patterns
- Friction gates
- Operational guardrails
- Structured workflows
- Transparent reasoning
- AI-assisted engineering discipline

The aim is not to slow innovation down.

The aim is to make rapid AI-assisted engineering sustainable and trustworthy.

A lot of current AI tooling focuses heavily on generation speed, but speed alone does not create trustworthy systems.

Generating code quickly is no longer the hard part.

Understanding it, trusting it, validating it, and operating it responsibly at scale is where the real engineering challenge starts to emerge.

As generation becomes cheaper and faster, the bottleneck increasingly moves toward:

- Human understanding
- Validation
- Operational confidence
- Governance
- Long-term maintainability
- Accountability

Part of this project is exploring whether engineering workflows can be designed differently through:

- Structured confidence models
- Graduated trust systems
- Risk-aware friction gates
- Validation pipelines
- Explicit operational context
- Better reasoning visibility
- Human review focused where it matters most

The goal is not blind automation.

The goal is reducing unnecessary cognitive load while keeping engineering standards high.

---

# Current State of the Project

This repository is currently in active development.

Some components are operational and already useful.
Others are experimental, incomplete, or currently exist as scaffolding for future implementation.

That is intentional.

Part of the purpose of this repository is documenting ideas, workflows, validation patterns, and architectural direction early, rather than waiting until every component is fully polished.

Expect:

- Rough edges
- Refactors
- Incomplete features
- Changing interfaces
- Iteration as concepts evolve

This is being developed openly and iteratively.

---

## Start Here

If this is your first time using the framework:

➡️ Read: `docs/QUICKSTART.md`

The quickstart gets you from:

- clean clone
- to a successful runtime execution
- in under 10 minutes

using the real runtime runner and adapter lifecycle.

---

# Existing Technical / Operational Sections

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
- execution telemetry event generation

Partially implemented runtime capabilities include:

- pre-execution token estimation

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

The framework intentionally separates:

- stable capability intent
from:
- unstable provider model identifiers

Provider model mappings are expected to evolve continuously and should be treated as configurable operational state rather than fixed framework truth.

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

The framework is currently focused on validating the runtime execution model, improving governance-aware observability, expanding adapter support, and strengthening the operational trust layer around AI-assisted delivery.

Longer-term roadmap items and future-state runtime capabilities are tracked in:

- `framework/FRAMEWORK-ROADMAP.md`

---

# License

This project is licensed under the MIT License.

See:
- `LICENSE`

---

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
