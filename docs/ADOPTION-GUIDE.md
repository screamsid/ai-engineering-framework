# Adoption Guide

## Goal

Adopt the framework without drowning the project in process.

The framework is designed so humans define:

- intent
- scope
- risk
- validation expectations
- escalation boundaries

The runtime handles:

- routing
- governance
- context compilation
- execution orchestration
- validation
- calibration
- telemetry

---

# Minimal Viable Adoption

1. Add the project template files
2. Complete the project profile
3. Pick a mode
4. Pick a preset
5. Use the planner, builder, and reviewer flow
6. Keep the audit log and backlog current

---

# Human Entry Workflow

## Step 1 — Fill In Human Task Entry

Start with:

```text
examples/python-automation/HUMAN-TASK-ENTRY.md
```

This captures:

- objective
- scope
- risk level
- validation requirements
- stop conditions
- escalation preferences

Humans should not need to manually configure runtime internals.

---

## Step 2 — Generate Runtime Call

Use:

```text
runtime/entry/runtime_call_builder.py
```

The builder:

- validates input
- applies safe defaults
- generates a valid `RUNTIME-CALL.yaml`

This creates the canonical runtime invocation contract.

---

## Step 3 — Execute Runtime

Invoke the runtime:

```bash
python -m runtime.runner
```

Current prototype behaviour:

- loads runtime task
- routes execution
- compiles context
- invokes adapter
- validates output
- applies calibration
- generates telemetry

---

# Current Safe Default

The safe default execution adapter is:

```text
mock
```

The mock adapter:

- performs no external execution
- performs no filesystem modification
- performs no API calls
- performs no token-consuming agent invocation

This allows lifecycle testing without execution risk.

---

# Current Prototype Boundaries

Real external execution adapters are scaffolded but not implemented yet:

- Codex
- Claude Code
- Antigravity

The runtime architecture is designed to support them through governed execution contracts.

---

# Gradual Adoption For Existing Projects

- Start with planning, audit logging, and handoffs
- Add security review and git checks next
- Add release checks once the project is mature enough to benefit

---

# Source Of Truth Rule

If a project changes the framework locally and the change is generally useful, feed it back into the framework repository.

---

# Core Principle

Humans provide:

- intent
- boundaries
- validation expectations

The runtime provides:

- governance
- orchestration
- execution management
- runtime enforcement

The framework should never rely on hidden assumptions.
