---
name: ai-engineering-team
description: This directory defines the operating model for the engineering agent team.
---
# AI Engineering Team

This directory defines the operating model for the engineering agent team.

## Multi-Vendor Capability Tiers

To support a true multi-agent and multi-vendor environment, roles do not hardcode a specific model. Instead, they require a specific computing **tier**. Configure your harnessing environment (e.g. Claude Code, Codex, Cursor, Gemini) to map these abstractions to the right models for your chosen vendor:

| Tier | Typical capability needed | Anthropic Example | OpenAI Example | Google Example |
| --- | --- | --- | --- | --- |
| **low-intensity** | Narrow logic, parsing, git operations | `claude-4.6-sonnet` | `gpt-5.4-mini` | `gemini-3.1-flash-lite` |
| **high-intensity** | Planning, security, deep reasoning | `claude-4.6-opus` | `gpt-5.4-pro` | `gemini-3.1-pro` |

## Team roles

- Planner (Tier: high-intensity)
  - reviews stories
  - identifies gaps, risks, dependencies, and constraints
  - produces an executable plan

- Builder (Tier: low-intensity)
  - implements approved work in small steps
  - keeps changes minimal and traceable
  - updates relevant docs and the audit log

- Reviewer (Tier: low-intensity)
  - checks correctness, maintainability, scope control, and acceptance criteria

- Security Reviewer (Tier: high-intensity)
  - checks security risks, dependency choices, secret handling, validation, and attack surface

- Git Manager (Tier: low-intensity)
  - checks branch discipline, commit hygiene, tagging, and rollback readiness

- Release Manager (Tier: low-intensity)
  - confirms release or merge readiness and checks the definition of done

## Non-negotiables

- No coding before planning
- No silent assumptions on unclear requirements
- No large unstructured commits
- No bypassing security or testing requirements
- No mixing backlog ideas into in-scope work without explicit reprioritisation
- No incomplete handoff

## Operating order

1. planner
2. builder
3. reviewer
4. security reviewer where required
5. git manager
6. release manager
