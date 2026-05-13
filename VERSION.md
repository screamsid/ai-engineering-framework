# Framework Version

Current Version: v0.4.0

## Release notes

### v0.4.0
- Implemented the Codex CLI adapter as the first real external execution adapter beyond the mock adapter
- Added Codex subprocess invocation with structured adapter result normalisation
- Added Codex governance enforcement for approval mode, filesystem write restrictions, timeout handling, model selection, and human validation checkpoints
- Hardened Codex approval-mode governance so high and critical risk tasks cannot use autonomous auto or full modes
- Added explicit Codex governance unit tests covering approval-mode constraints
- Added mocked Codex subprocess tests for successful invocation, timeout handling, malformed output handling, missing CLI handling, and registry lookup
- Added routing_config propagation from runtime tasks into adapter payloads
- Added explicit runner test coverage proving approval mode, timeout, model, and filesystem write settings reach adapters
- Extracted the Codex default model into a named constant
- Documented Codex CLI flag assumptions and version-compatibility risks in the adapter
- Added `docs/QUICKSTART.md` as the primary onboarding path for running the framework locally
- Added `docs/SURGICAL-IMPLEMENTATION.md` to document the surgical implementation pattern for safe changes in existing codebases
- Added the `surgical-implementation` routing task type with conservative defaults
- Added the `presets/surgical-implementation/` preset covering read-first discipline, minimal blast radius, and mandatory diff review
- Updated `docs/QUICKSTART.md` to position surgical implementation as a primary use case alongside greenfield development
- Updated the README to clearly frame the project as an active prototype and engineering exploration into AI-assisted trust, governance, and operational safety
- Clarified token estimation and telemetry maturity in the README, including current approximation limits and planned token cost tracking
- Added MIT licence file and README licence section

### v0.3.2
- Updated repository README to reflect current runtime architecture
- Updated documented repository structure to match actual runtime layout
- Clarified implemented versus planned framework capabilities
- Documented runtime execution lifecycle and orchestration flow
- Clarified future-state governance documents with planned capability markers
- Added roadmap references for future runtime concepts

### v0.3.1
- Wired ContextCompiler into RuntimeRunner execution lifecycle
- Wired MemoryLoader into runtime context assembly
- Added embedded seed memory support for prototype execution
- Wired TokenEstimator into adapter invocation flow
- Wired ExecutionTelemetry into runtime execution lifecycle
- Added runtime token warning support
- Added telemetry event output to runtime_result
- Added runtime runner integration coverage
- Added HUMAN-TASK-ENTRY worked example
- Added RuntimeCallBuilder end-to-end entry tests
- Fixed duplicate validation errors for missing risk_level
- Aligned RuntimeCallBuilder output with invocation schema and worked example
- Centralised framework version lookup via VERSION.md

### v0.3.0
- Added execution adapter abstraction layer
- Added base adapter interface
- Added adapter invocation contract schema
- Added adapter result schema
- Added mock execution adapter for safe runtime lifecycle testing
- Added Codex adapter scaffold
- Added Claude Code adapter scaffold
- Added Antigravity adapter scaffold
- Added adapter registry for provider isolation
- Wired runtime runner to invoke adapters through registry
- Replaced direct runner stub path with adapter-driven execution
- Added adapter execution tests
- Added context compiler for minimal runtime context generation
- Added runtime invocation examples
- Added memory relevance loader
- Added lightweight token estimator
- Added runtime execution telemetry collector
- Preserved explicit prototype boundaries for real external agent execution

### v0.2.1
- Fixed critical risk handling in confidence gates
- Fixed calibration integrity so validation outcomes drive confidence adjustment
- Externalised calibration policy and rationale into configuration
- Added runtime component tests for gates, calibration, router, and runner
- Added requirements.txt for runtime dependencies
- Added portable test package marker for CI compatibility
- Clarified prototype runtime boundaries and stub execution limitations
- Added explicit router precedence and overwrite-order rules
- Added runtime invocation example via RUNTIME-CALL.yaml
- Completed worked Python automation lifecycle example
- Added Memory Reviewer role definition
- Wired Formatter role into operational workflow
- Added future-runtime maturity labelling for conceptual capabilities
- Replaced deprecated utcnow() usage for future Python compatibility
- Improved governance transparency and runtime auditability

### v0.2.0
- Added runtime governance architecture
- Added confidence ratings and confidence gates
- Added risk classification and confidence calibration guidance
- Added framework memory, memory feedback loop, and memory lifecycle standards
- Added agent adherence and drift control standards
- Added friction control principle: Block on risk. Warn on style. Learn from everything.
- Added Formatter role with no-interpretation and no-spin constraints
- Added runtime role cards and role-card schema
- Added canonical structured output schema
- Added runtime loaders, router, confidence gate, validator, formatter, audit logger, and calibration store prototypes
- Added deterministic routing rules and agent registry
- Added validator tests
- Strengthened security-tool and infrastructure-automation presets
- Added root .gitignore
- Started worked Python automation example

### v0.1.0
- Initial framework structure
- Core rules and workflow created
- Role definitions created
- Project templates created
- Modes and project presets created
- Adoption guidance created
