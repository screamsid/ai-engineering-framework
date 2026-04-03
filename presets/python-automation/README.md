# Python Automation Preset

Recommended for internal Python tooling, automation scripts, collectors, and operational utilities.

## Defaults
- Project class: automation
- Risk tier: medium by default
- Preferred mode: standard
- Typical commands:
  - install: `python -m pip install -r requirements.txt`
  - lint: project-defined, for example `ruff check .`
  - test: project-defined, for example `pytest`
  - smoke test: run the primary command in a safe or dry-run mode

## Focus areas
- safe command execution
- secrets handling
- dependency discipline
- logging hygiene
- clear error handling
