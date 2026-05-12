# Human Entry Point

The human entry point defines how a person starts a framework task without needing to understand the internal runtime machinery.

## Decision

For v0.3.1, the entry point is:

- structured human task template
- minimal runtime call builder
- validation before runtime ingestion
- generated `RUNTIME-CALL.yaml`

This is intentionally not a full CLI, GUI, or automation workflow yet.

## Why This Approach

A structured template keeps the entry point:

- human-readable
- agent-compatible
- low-friction
- easy to review
- easy to convert into runtime input
- vendor-neutral

## Human Entry Flow

```text
Human intent
  ↓
Task entry template
  ↓
Runtime call builder
  ↓
Validation
  ↓
RUNTIME-CALL.yaml
  ↓
Runtime execution
```

## Core Principle

Humans describe intent and governance boundaries.

They should not need to manually understand:

- adapter contracts
- telemetry internals
- calibration logic
- memory lifecycle internals
- orchestration machinery

## Minimal Required Human Inputs

- task id
- task type
- objective
- scope
- risk level
- confidence score
- validation expectations
- stop conditions

## Safety Rule

The entry point must validate input before generating a runtime call.

Invalid or incomplete human input should not silently become runtime execution.
