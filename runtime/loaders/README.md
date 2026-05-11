# Runtime Loaders

Runtime loaders assemble the minimal operational context required for an agent task.

The goal is to:

- reduce context bloat
- reduce agent drift
- load only relevant governance
- improve runtime consistency
- support confidence-gated execution

## Loader Types

### Role Loader

Loads:

- role card
- required outputs
- stop conditions
- escalation rules
- confidence thresholds

### Skill Loader

Loads:

- relevant skill packs
- validation expectations
- role-specific execution guidance

### Memory Loader

Loads:

- relevant framework memory
- reusable lessons
- anti-patterns
- calibration guidance

Memory loading should remain selective.

Do not inject unrelated or stale memory.

### Rule Loader

Loads:

- required framework rules
- runtime enforcement guidance
- confidence requirements
- escalation controls

## Runtime Assembly Flow

```text
Task arrives
  ↓
Risk classification
  ↓
Role Loader
  ↓
Skill Loader
  ↓
Rule Loader
  ↓
Memory Loader
  ↓
Minimal runtime context assembled
  ↓
Agent execution
```

## Minimal Context Principle

The runtime should inject:

- only relevant rules
- only relevant skills
- only useful memory
- only required outputs

Large static context should be avoided.

## Loader Anti-Patterns

Avoid:

- loading the entire framework every task
- loading every memory item
- overlapping rule duplication
- deeply nested orchestration chains
- runtime recursion loops

## Completion Rule

Runtime loaders are successful when agents receive enough context to remain aligned without overwhelming reasoning capacity.
