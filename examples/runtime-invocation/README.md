# Runtime Invocation Examples

These examples show how to invoke the runtime without loading the full framework into an agent context.

The goal is to demonstrate:

- deterministic routing
- adapter selection
- confidence-gated execution
- minimal context assembly
- mock execution without token burn

## Examples

```text
examples/runtime-invocation/
├── README.md
├── mock-runtime-task.yaml
├── preferred-adapter-task.yaml
└── critical-risk-task.yaml
```

## Safe Default

The safe default adapter is `mock`.

The mock adapter performs no external calls, no CLI execution, no filesystem writes, and no token usage.

## Invocation Pattern

```bash
python -m runtime.runner
```

Current prototype behaviour:

- loads `examples/runtime-task.yaml` by default
- routes the task
- invokes the configured adapter
- validates adapter output
- applies calibration
- formats a human-readable result

## Adapter Selection

Use:

```yaml
runtime:
  adapter: mock
```

or:

```yaml
runtime:
  adapter: preferred
```

`preferred` uses the runtime router decision.

Real Codex, Claude Code, and Antigravity execution adapters are scaffolded but not implemented yet.
