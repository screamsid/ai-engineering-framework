# Testing Standards

## Minimum requirement
Every change must pass a smoke test appropriate to the work.

## Test levels
- Smoke tests for every story
- Unit tests where logic changes
- Integration tests where interfaces or workflows change
- Security validation where attack surface changes

## Builder responsibilities
Builder must document:
- what was tested
- how it was tested
- what was not tested
- why any testing gap exists

## Reviewer responsibilities
Reviewer must confirm testing is proportionate to risk.

## Prohibited
- claiming work is complete without validation
- untested changes to critical paths
