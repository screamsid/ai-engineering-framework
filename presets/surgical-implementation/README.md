# Surgical Implementation Preset

The surgical-implementation preset is designed for modifying existing systems safely.

This preset assumes:

- an existing codebase already exists
- operational stability matters
- blast radius should remain minimal
- reviewers need clear visibility into changes
- uncertainty should be declared explicitly

The goal is not maximum autonomy.

The goal is safe targeted iteration.

---

# Default Behaviour

The preset biases toward conservative execution.

Defaults include:

- reviewer-required routing
- human validation checkpoints
- suggest-mode execution
- validation-first workflow
- mandatory known gaps output
- mandatory rollback visibility
- explicit out_of_scope boundaries

---

# Read-First Discipline

The preset expects:

- existing code reviewed before modification
- dependency awareness before change
- explicit scope boundaries before execution

The framework assumes:

> nothing outside the declared scope should be modified.

---

# Minimal Blast Radius

The preset encourages:

- isolated module changes
- narrow context loading
- selective dependency visibility
- targeted validation

Large-scale refactors should be split into smaller surgical tasks where possible.

---

# Mandatory Diff Review

The surgical preset assumes:

```yaml
stop_conditions:
  - unreviewed_diff
```

Human review is considered mandatory before merge.

Especially for:

- infrastructure automation
- security-sensitive changes
- legacy systems
- production-impacting behaviour

---

# Recommended Governance Defaults

Example:

```yaml
governance:
  risk_level: medium
  confidence_threshold: 90
```

Example routing:

```yaml
routing:
  adapter: codex
  approval_mode: suggest
```

These defaults intentionally bias toward:

- visibility
- reviewability
- safe iteration

rather than autonomous modification.
