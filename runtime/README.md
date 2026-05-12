# Runtime

The runtime layer turns the framework from static guidance into callable operational controls.

It exists so an agent harness can:

- classify work
- select roles
- load concise rule cards
- load relevant skill packs
- compile execution context
- estimate payload size before adapter invocation
- emit execution telemetry
- apply confidence gates
- validate required outputs
- request human validation when needed
- record calibration data
- propose safe memory updates

## Runtime Components

```text
runtime/
├── README.md
├── invocation/
│   └── framework-call.schema.yaml
├── rules/
│   ├── rule-card.schema.yaml
│   ├── builder.rule-card.yaml
│   ├── reviewer.rule-card.yaml
│   ├── security-reviewer.rule-card.yaml
│   ├── memory-reviewer.rule-card.yaml
│   └── release-manager.rule-card.yaml
├── validators/
│   ├── output-validation.schema.yaml
│   └── required-output-sections.yaml
└── telemetry/
    └── calibration-record.schema.yaml
```

## Operating Flow

```text
Task arrives
  ↓
Create framework call
  ↓
Classify risk
  ↓
Select role
  ↓
Load role card
  ↓
Load relevant skill packs
  ↓
Load relevant memory
  ↓
Assemble runtime context
  ↓
Compile execution context
  ↓
Estimate adapter payload size
  ↓
Invoke adapter
  ↓
Validate output
  ↓
Apply confidence gate
  ↓
Record calibration data
  ↓
Emit execution telemetry
  ↓
Escalate to human if needed
  ↓
Propose memory updates if useful
```

## Story 003 Prototype Scope

Story 003 wires the following runtime components into `RuntimeRunner`:

- `ContextCompiler`
- `MemoryLoader`
- `TokenEstimator`
- `ExecutionTelemetry`

The runner should pass compiled context to adapters rather than raw assembled context.

Relevant memory items are loaded from embedded seed data and included in both the runtime context and compiled context.

Token estimates are calculated before adapter invocation. If the estimate exceeds the threshold, a warning is surfaced in `runtime_result`.

Execution telemetry is built after adapter execution, validation, and calibration. The telemetry event is included in `runtime_result`.

## Story 003 Known Limitations

Hardcoded seed memory in `RuntimeRunner.__init__()` is an accepted prototype smell for Story 003.

This keeps blast radius low and unblocks wiring the full execution path.

The following are explicitly deferred to a future story:

- memory provider abstraction
- external memory source integration
- deterministic memory fixtures for isolated tests
- runtime-scoped memory loading per task context
- memory scoring or decay
- domain trust profiling
- persistent telemetry storage beyond the existing runtime outputs

## Design Principles

- Keep injected context small.
- Do not dump the full framework into every prompt.
- Enforce only high-value controls first.
- Confidence controls autonomy.
- Human validation outcomes become calibration data.
- Memory promotion must be sanitised and reviewed.
- Runtime controls should reduce risk without blocking safe delivery.

## Initial Enforcement Scope

The first runtime implementation should enforce:

- confidence gate present
- risk level present
- validation summary present
- known gaps present
- handoff present
- human validation below threshold
- security review for high-risk work

## Non-Hindrance Rule

The runtime must not become a ceremony engine.

It should help agents stay aligned, not bury delivery in process.
