---
name: security-tool-preset
description: Recommended for scanners, security automation, detection tooling, defensive utilities, authorised testing tools, and other higher-scrutiny projects.
---
# Security Tool Preset

Recommended for scanners, security automation, detection tooling, defensive utilities, authorised testing tools, and other higher-scrutiny projects.

## Defaults

- Project class: security-tool
- Risk tier: high by default
- Preferred mode: full
- Security review: required
- Confidence threshold: high

## Core Focus Areas

- auth and privilege boundaries
- secure logging and evidence handling
- safe storage of secrets and tokens
- careful dependency review
- clear operator warnings and guardrails
- explicit scope enforcement
- authorised target boundaries
- safe result retention
- output sanitisation
- abuse prevention

## Scope Enforcement

Security tools must not run against undefined or unauthorised targets.

Projects should define:

- permitted target types
- excluded target types
- required operator confirmation
- safe default mode
- dry-run mode where possible
- evidence of authorisation where appropriate

## Offensive or Dual-Use Tooling

For offensive, red-team, Bluetooth, wireless, scanner, exploit-testing, or recon-style tools:

- require explicit scope boundaries
- avoid hardcoded targets
- avoid automatic attack execution
- require deliberate operator action for intrusive behaviour
- log operator intent where appropriate
- preserve evidence safely
- avoid storing sensitive target data unnecessarily
- sanitise output before sharing or committing

## Logging and Evidence Handling

Logs and evidence must be handled carefully.

Consider:

- sensitive hostnames
- IP addresses
- usernames
- tokens
- session IDs
- packet captures
- scan results
- screenshots
- exploit output

Default behaviour should minimise unnecessary retention.

## Stop Conditions

Stop or escalate when:

- scope is unclear
- authorisation is unclear
- intrusive behaviour is possible
- secrets or sensitive data may be exposed
- output could identify real targets unintentionally
- confidence is below the required threshold

## Validation Expectations

Security-tool projects should validate:

- safe default behaviour
- scope checks
- logging sanitisation
- dry-run behaviour
- permission handling
- failure handling
- evidence retention controls

## Memory Candidates

Reusable lessons from security-tool projects should be sanitised before framework promotion.

Do not promote:

- targets
- exploit details tied to real environments
- customer or internal infrastructure data
- sensitive scan results
- credentials or tokens
