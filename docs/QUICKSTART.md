# Quickstart

This guide gets you from:

- clean clone
- to a successful runtime execution
- in under 10 minutes

You will:

1. install the framework
2. run the worked example
3. generate your own runtime call
4. execute it through the runtime runner
5. understand what happened

The quickstart uses the mock adapter by default because it is the safest prototype execution path.

The framework now also includes a real Codex CLI adapter implementation.

For deeper framework concepts, see:

- `README.md`
- `runtime/README.md`
- `framework/FRAMEWORK-ROADMAP.md`

---

# Prerequisites

Required:

- Python 3.11+
- Git

Optional but recommended:

- virtual environment support
- VS Code or PyCharm
- Codex CLI installed and authenticated

---

# Clone the Repository

```bash
git clone https://github.com/screamsid/ai-engineering-framework.git

cd ai-engineering-framework
```

---

# Create a Virtual Environment

Linux/macOS:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv

.venv\Scripts\Activate.ps1
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Current dependencies are intentionally lightweight.

---

# Run the Worked Example

Run the runtime runner:

```bash
python runtime/runner.py
```

You should see:

- runtime_result
- routing decision
- validation result
- telemetry event
- human_output

The default execution path uses the mock adapter.

This validates the governance-aware runtime lifecycle without calling external providers.

---

# What Just Happened?

The framework executed a full governance-aware runtime lifecycle.

```text
runtime-task.yaml
  ↓
RuntimeRunner loaded the task
  ↓
Router selected role + adapter
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
```

Even though the default adapter is mocked, the governance lifecycle is real.

That means you can safely:

- test runtime orchestration
- validate routing
- validate governance controls
- test calibration behaviour
- test telemetry flow
- evolve the runtime architecture

without depending on external providers.

---

# Create Your Own Task

Use the worked example:

- `examples/python-automation/HUMAN-TASK-ENTRY.md`

as a template.

Example minimal task input:

```python
from runtime.entry.runtime_call_builder import RuntimeCallBuilder

builder = RuntimeCallBuilder()

runtime_call = builder.build(
    {
        "task_id": "STORY-999",
        "task_type": "python-automation",
        "objective": "Build a CSV inventory parser",
        "scope": [
            "Parse CSV input",
            "Add validation",
        ],
        "risk_level": "low",
        "confidence_score": 90,
        "validation_requirements": [
            "smoke-test",
        ],
        "stop_conditions": [
            "validation_missing",
        ],
    }
)

print(builder.to_yaml(runtime_call))
```

---

# Generate a Runtime Call

Save the generated YAML as:

```text
examples/my-runtime-task.yaml
```

You can also generate runtime calls directly inside your own tooling or harness.

---

# Run Your Task

Run the runtime runner against your generated runtime call:

```bash
python runtime/runner.py
```

Current prototype behaviour:

- default adapter = mock
- telemetry is runtime-only
- embedded seed memory is used
- governance constraints are enforced before adapter execution

---

# Try the Codex Adapter

The framework now includes a real Codex CLI adapter implementation.

Prototype status:
- implemented
- subprocess-backed
- governance-aware
- tested with mocked subprocess execution
- not yet operationally validated against real workloads

Example routing block:

```yaml
routing:
  adapter: codex
  approval_mode: suggest
  timeout_seconds: 300
  allow_filesystem_write: false
  model: gpt-5
```

Example invocation flow:

```text
RuntimeRunner
  ↓
CodexAdapter
  ↓
Codex CLI subprocess
```

Governance enforcement examples:

- high-risk tasks cannot use unsafe autonomous mode
- filesystem-write restrictions downgrade execution mode automatically
- human validation checkpoints are enforced in runtime state

Important:
- the Codex CLI must already be installed
- the Codex CLI must already be authenticated
- the adapter returns structured errors if Codex is unavailable

Until real-task validation is complete:
- mock remains the safest default
- Codex should be treated as prototype execution

---

# Run the Tests

```bash
pytest
```

The test suite uses mocked subprocess execution.

No real Codex CLI is required for CI.

---

# Next Steps

Once you are comfortable with the runtime lifecycle:

Explore:

- `runtime/adapters/`
- `runtime/rules/`
- `runtime/router/`
- `runtime/memory/`
- `runtime/calibration/`

Then look at:

- presets
- modes
- skill packs
- adapter integration
- runtime governance expansion
- framework compliance automation
- future memory provider abstraction

---

# Prototype Boundaries

The current runtime is intentionally lightweight.

Current prototype limitations include:

- mock adapter remains default execution path
- Codex adapter not yet operationally validated
- embedded seed memory
- no persistent telemetry backend
- conceptual trust profiling only
- conceptual telemetry analytics only

These constraints keep the runtime:

- testable
- understandable
- low-blast-radius
- easy to evolve safely

---

# Final Note

This framework is not trying to create:

- AI ceremony
- giant prompts
- governance theatre

The goal is:

- bounded adaptive autonomy
- lightweight runtime governance
- safer AI-assisted delivery
- durable operational learning
