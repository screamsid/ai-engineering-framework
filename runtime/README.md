# Runtime

The runtime layer turns the framework from static guidance into callable operational controls.

It exists so an agent harness can:

- classify work
- select roles
- load concise rule cards
- load relevant skill packs
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
Inject minimal rules
  ↓
Agent performs work
  ↓
Validate output
  ↓
Apply confidence gate
  ↓
Escalate to human if needed
  ↓
Record calibration data
  ↓
Propose memory updates if useful
```

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
