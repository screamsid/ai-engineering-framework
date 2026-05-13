# Framework Version

Current Version: v0.3.1

## Release notes

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
