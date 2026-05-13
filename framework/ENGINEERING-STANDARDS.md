---
name: engineering-standards
description: Standard file for engineering-standards
---
# Engineering Standards

This document defines implementation-level engineering expectations for the framework.

The goal is not stylistic perfection.
The goal is operationally understandable, maintainable, low-blast-radius engineering.

A useful standard tells an engineer or agent:

- what good looks like
- what bad looks like
- why the difference matters

The examples below use Python because it is currently the framework's primary implementation language.

---

# Naming Standards

## Rule
Names should describe:

- intent
- behaviour
- data meaning
- operational purpose

A reader should understand what something does without opening five other files.

## Bad
```python

def process(data):
    return data.get("x")


n = len(devices)
flag = True
```

Problems:
- `process` says nothing about behaviour
- `data` gives no domain meaning
- `x` is meaningless outside local context
- `n` forces the reader to infer meaning
- `flag` does not describe state

## Good
```python

def extract_primary_ip(device_record: dict) -> str:
    return device_record.get("primary_ip", "")


connected_device_count = len(devices)
is_validation_enabled = True
```

Benefits:
- function describes exactly what it extracts
- variable names describe real operational meaning
- booleans read like questions
- code becomes understandable without tribal knowledge

## Guidance

Prefer:

- `parse_inventory`
- `load_runtime_config`
- `validate_firewall_rules`
- `has_validation_errors`
- `is_dry_run`

Avoid:

- `process`
- `handle`
- `do_thing`
- `tmp`
- `misc`
- `data2`

---

# Function Design

## Rule
Functions should have:

- one responsibility
- explicit inputs
- explicit outputs
- predictable side effects

A function that parses data should not also write files, update databases, and send notifications.

## Bad
```python

def parse_switch_inventory(config_path: str):
    with open(config_path) as f:
        inventory = json.load(f)

    with open("inventory-backup.json", "w") as backup:
        json.dump(inventory, backup)

    requests.post(
        "https://hooks.example.com/notify",
        json={"status": "loaded"},
    )

    return inventory
```

Problems:
- hidden filesystem writes
- hidden network calls
- impossible to reuse safely
- difficult to test in isolation
- unclear operational blast radius

## Good
```python

def load_switch_inventory(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)



def write_inventory_backup(inventory: dict, backup_path: str) -> None:
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)



def send_inventory_notification(webhook_url: str) -> None:
    requests.post(
        webhook_url,
        json={"status": "inventory_loaded"},
        timeout=10,
    )
```

Benefits:
- responsibilities separated cleanly
- side effects are explicit
- individual functions are testable
- blast radius stays small
- reuse becomes safe and predictable

## Guidance

Prefer:
- explicit return values
- dependency injection
- small composable helpers
- pure functions where practical

Avoid:
- hidden global state
- filesystem writes during parsing
- functions that mutate unrelated objects
- large multi-purpose utility functions

---

# Error Handling

## Rule
Fail clearly.
Return useful errors.
Never swallow exceptions silently.

The caller should know:

- what failed
- where it failed
- why it failed
- whether recovery is possible

## Bad
```python

def load_runtime_config(config_path):
    try:
        with open(config_path) as f:
            return json.load(f)
    except Exception:
        return {}
```

Problems:
- catches everything
- hides the actual failure
- caller cannot distinguish:
  - missing file
  - invalid JSON
  - permission issue
- silent fallback behaviour creates operational drift

## Good
```python

class RuntimeConfigError(Exception):
    pass



def load_runtime_config(config_path: str) -> dict:
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError as exc:
        raise RuntimeConfigError(
            f"Runtime config not found: {config_path}"
        ) from exc

    except json.JSONDecodeError as exc:
        raise RuntimeConfigError(
            f"Invalid JSON in runtime config {config_path}: {exc}"
        ) from exc
```

Benefits:
- failure mode is explicit
- caller receives useful context
- debugging time is reduced
- operational telemetry becomes meaningful

## Additional Guidance

### Do not use bare except

## Bad
```python
try:
    run_task()
except:
    pass
```

This catches:
- programming errors
- interrupts
- runtime failures
- unrelated unexpected conditions

## Good
```python
try:
    run_task()
except RuntimeTaskError as exc:
    logger.error("Runtime task failed", extra={"error": str(exc)})
    raise
```

### Do not log and continue silently

## Bad
```python
try:
    validate_runtime_call(payload)
except Exception as exc:
    logger.error(exc)
```

Execution continues even though validation failed.

## Good
```python
try:
    validate_runtime_call(payload)
except ValidationError as exc:
    logger.error(
        "Runtime validation failed",
        extra={"validation_error": str(exc)},
    )
    raise
```

Validation failure stops execution clearly.

---

# Configuration Management

## Rule
Configuration belongs outside code.

Never hardcode:

- credentials
- tokens
- API keys
- environment-specific paths
- production URLs
- ports
- secrets

Configuration should be:

- environment-driven
- explicit
- reviewable
- replaceable without code changes

## Bad
```python
API_KEY = "super-secret-key"
DATABASE_HOST = "10.10.10.5"
LOG_PATH = "/home/simon/runtime.log"
```

Problems:
- secrets exposed in source control
- environment coupling
- impossible to deploy safely across environments
- difficult rotation and lifecycle management

## Good
```python
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("RUNTIME_API_KEY")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
LOG_PATH = os.getenv("LOG_PATH", "logs/runtime.log")

if not API_KEY:
    raise RuntimeError("RUNTIME_API_KEY environment variable is required")
```

Benefits:
- secrets separated from code
- runtime remains portable
- defaults are explicit
- deployment becomes environment-aware

## Additional Guidance

### .env handling

`.env` files:
- are for local development convenience
- must never be committed
- must exist in `.gitignore`
- should contain example placeholders only when documented publicly

Example:
```env
RUNTIME_API_KEY=replace-me
DATABASE_HOST=localhost
LOG_LEVEL=INFO
```

### Configuration validation

Validate critical configuration during startup.

## Bad
```python
api_key = os.getenv("API_KEY")
```

Failure appears much later during runtime.

## Good
```python
api_key = os.getenv("API_KEY")

if not api_key:
    raise RuntimeError("Missing required environment variable: API_KEY")
```

---

# Logging Discipline

## Rule
Logs are operational evidence.

Logging should:
- help investigation
- support debugging
- improve observability
- preserve operational context

Use structured logging.
Do not use `print()` for runtime behaviour.

## Bad
```python
print("task failed")
```

Problems:
- no timestamp
- no severity
- no context
- not machine searchable
- inconsistent operational visibility

## Good
```python
import logging


logger = logging.getLogger(__name__)


logger.error(
    "Runtime validation failed",
    extra={
        "task_id": runtime_call["task"]["id"],
        "risk_level": runtime_call["governance"]["risk_level"],
        "validation_stage": "schema_validation",
    },
)
```

Benefits:
- structured operational context
- machine-readable telemetry
- searchable events
- useful incident investigation trail

## Never Log

The following must never appear in logs:

- passwords
- API tokens
- session cookies
- private keys
- raw authentication headers
- full raw request bodies
- personally identifiable information
- secrets from `.env`

## Bad
```python
logger.info(f"Using API key: {api_key}")
logger.debug(f"Full request body: {request.text}")
```

## Good
```python
logger.info("API client initialised")

logger.debug(
    "Runtime request received",
    extra={
        "request_size": len(request.text),
        "task_type": runtime_call["task"]["type"],
    },
)
```

Log useful operational metadata.
Do not log sensitive payload content.

---

# Module Structure

## Rule
Modules should have:

- one clear responsibility
- predictable location
- minimal cross-coupling
- explicit public interfaces

## Bad
```text
utils.py
helpers.py
misc.py
```

Problems:
- unclear ownership
- mixed responsibilities
- difficult navigation
- impossible dependency boundaries

## Good
```text
runtime/
├── adapters/
│   ├── codex_adapter.py
│   ├── mock_adapter.py
│   └── __init__.py
├── validation/
│   ├── runtime_validator.py
│   └── schema_loader.py
└── telemetry/
    ├── execution_telemetry.py
    └── token_estimator.py
```

Benefits:
- responsibility boundaries are obvious
- operational ownership becomes clearer
- onboarding becomes easier
- blast radius remains constrained

## __init__.py Guidance

Export only the intended public interface.

## Bad
```python
from .codex_adapter import *
from .mock_adapter import *
```

## Good
```python
from .codex_adapter import CodexAdapter
from .mock_adapter import MockAdapter

__all__ = [
    "CodexAdapter",
    "MockAdapter",
]
```

---

# Change Discipline

## Rule
Engineering discipline matters more than implementation speed.

This framework explicitly prioritises:

- small safe changes
- limited blast radius
- explicit scope control
- reviewability
- rollback readiness

This section directly reinforces:

- `CORE-RULES.md` Rule 3: small safe steps
- `CORE-RULES.md` Rule 4: keep scope tight
- `CORE-RULES.md` Rule 5: new ideas go to backlog

## Bad
Story:
- fix runtime validation bug

Actual PR:
- fixes validation bug
- rewrites adapter architecture
- renames modules
- reformats unrelated files
- changes logging framework
- adds experimental telemetry work

Problems:
- impossible review scope
- unclear failure source
- rollback complexity increased
- operational risk hidden inside unrelated changes

## Good
Story:
- fix runtime validation bug

PR:
- fixes validation bug only
- adds targeted regression test
- documents behavioural change
- logs unrelated refactor ideas into backlog
```
Backlog:
- STORY-REF-014: simplify adapter loading architecture
- STORY-OBS-003: improve telemetry formatting
```

Benefits:
- reviewer focus stays narrow
- rollback remains simple
- regression source becomes obvious
- architectural ideas are preserved without scope creep

## Guidance

If you discover additional improvements while implementing a task:

- document them
- backlog them
- do not silently expand scope

Exception:
Only expand scope when required for:
- correctness
- security
- safe implementation
- unavoidable dependency resolution

If scope must expand:
- document why clearly
- keep the expansion minimal
- ensure reviewers can distinguish required changes from optional changes

---

# Final Principle

Good engineering is not:
- cleverness
- abstraction count
- shortest code
- newest pattern

Good engineering is:
- understandable
- reviewable
- recoverable
- observable
- maintainable
- safe to operate

Optimise for the engineer maintaining the system six months later under operational pressure.
