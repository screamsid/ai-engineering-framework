# Security Standards

## Core principles
- least privilege
- secure defaults
- input validation
- output encoding where needed
- dependency awareness
- no secrets in code or logs

## Mandatory checks
- Validate all external inputs.
- Treat file paths, command execution, deserialisation, and template rendering as high risk.
- Avoid dynamic execution unless explicitly required and tightly controlled.
- Confirm authorisation boundaries for privileged actions.
- Ensure logs do not leak credentials, tokens, keys, or sensitive data.

## Dependency controls
- Prefer maintained libraries with active support.
- Avoid unnecessary packages.
- Review dependency risk before introducing new libraries.

## Data handling
- Minimise sensitive data exposure.
- Use redaction where needed.
- Do not log secrets or private tokens.

## Security review triggers
Mandatory security review for:
- authentication changes
- authorisation changes
- secrets handling
- file upload or parsing
- network listeners
- shell or subprocess calls
- dependency additions
- API integrations
