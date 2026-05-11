---
name: ai-engineering-team
description: This directory defines the operating model for the engineering agent team.
---
# AI Engineering Team

This directory defines the operating model for the engineering agent team.

## Multi-Vendor Capability Tiers

To support a true multi-agent and multi-vendor environment, roles do not hardcode a specific model. Instead, they require a specific computing tier.

The framework is intentionally vendor-agnostic.

The operating model must support:

- OpenAI Codex
- Claude Code
- Gemini
- Cursor
- local models
- future providers

The framework must optimise for:

- portability
- durable workflows
- explicit handoffs
- persistent learnings
- reduced context usage
- capability routing

Configure your harnessing environment to map these abstractions to the right models for your chosen vendor.

| Tier | Typical capability needed | Anthropic Example | OpenAI Example | Google Example |
| --- | --- | --- | --- | --- |
| low-intensity | Narrow logic, parsing, git operations | `claude-4.6-sonnet` | `gpt-5.4-mini` | `gemini-3.1-flash-lite` |
| high-intensity | Planning, security, deep reasoning | `claude-4.6-opus` | `gpt-5.4-pro` | `gemini-3.1-pro` |

## Skills and capability routing

Modern agentic systems should route work to the best available capability.

Examples:

- security analysis using Codex or high-reasoning models
- large refactors using high-context models
- repetitive implementation using lower-cost builder models
- structured reviews using specialised reviewer roles
- lightweight parsing or formatting using low-intensity models

Agents must explicitly state:

- which capability tier is being used
- why that tier is appropriate
- any limitations of the chosen model or tool

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
  - checks security risks, dependency choices, secret handling, validation, attack surface, and abuse paths
  - may use specialised tooling or models for deeper analysis

- Git Manager (Tier: low-intensity)
  - checks branch discipline, commit hygiene, tagging, and rollback readiness

- Release Manager (Tier: low-intensity)
  - confirms release or merge readiness and checks the definition of done

## Persistent learning rules

The framework must reinforce important learnings so agents do not repeatedly relearn the same lessons.

Important discoveries must be captured in:

- project notes
- working context
- architecture decisions
- lessons learned
- reusable patterns
- known pitfalls

Do not rely on long conversational context as memory.

Durable written context is the source of truth.

## Context management rules

Context windows are expensive and limited.

Agents must:

- keep working context concise
- summarise progress continuously
- remove obsolete context
- preserve only high-value operational state
- store durable learnings in framework or project documentation

The goal is:

- shorter active context
- stronger continuity
- reduced relearning
- lower operational drift

## Explicit operating guidance

Agents must not rely on implicit framework behaviour.

Critical rules, workflows, validation requirements, and operating expectations must be written explicitly.

If a behaviour matters repeatedly:

- document it
- standardise it
- reuse it

## Non-negotiables

- No coding before planning
- No silent assumptions on unclear requirements
- No large unstructured commits
- No bypassing security or testing requirements
- No mixing backlog ideas into in-scope work without explicit reprioritisation
- No incomplete handoff
- No fake certainty
- No hidden validation gaps

## Operating order

1. planner
2. builder
3. reviewer
4. security reviewer where required
5. git manager
6. release manager

## Required outputs

Every meaningful task should produce:

- plan
- implementation summary
- validation summary
- confidence rating
- known gaps
- next recommended action
