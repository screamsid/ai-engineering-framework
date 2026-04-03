# Engineering Standards

## General
- Prefer small, composable functions and modules.
- Avoid unnecessary abstraction.
- Keep naming explicit and consistent.
- Keep side effects obvious.
- Document non-obvious decisions.

## Change discipline
- Change only what the story requires.
- Avoid opportunistic refactors unless needed for safe implementation.
- If a refactor is necessary, document why.

## Readability
- Code should be understandable by another engineer without tribal knowledge.
- Prioritise clarity over novelty.

## Error handling
- Fail clearly.
- Return useful errors.
- Avoid swallowing exceptions or hiding failure modes.

## Configuration
- Keep configuration separate from code.
- Do not hard-code secrets.
- Use environment-driven configuration where appropriate.

## Documentation
- Update documentation when behaviour, workflow, or architecture changes.
- Keep docs close to the code where practical.
