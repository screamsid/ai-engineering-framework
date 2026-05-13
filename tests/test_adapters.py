import subprocess
from unittest.mock import Mock, patch

from runtime.adapters.codex_adapter import CodexAdapter
from runtime.adapters.mock_adapter import MockAdapter
from runtime.adapters.registry import AdapterRegistry
from runtime.runner import RuntimeRunner


VALID_CODEX_OUTPUT = """
## Implementation Summary
Implemented CLI parsing.

## Validation Summary
Smoke tests passed.

## Confidence Gate
Confidence: 90%

## Known Gaps
- No integration tests yet.

## Handoff
Ready for review.
"""



def test_mock_adapter_returns_standard_result():
    adapter = MockAdapter()

    payload = {
        "task": {
            "id": "STORY-001",
            "objective": "Build inventory summary CLI",
        },
        "governance": {
            "confidence_score": 92,
            "human_validation_required": False,
        },
    }

    result = adapter.invoke(payload)

    assert result["adapter"]["name"] == "mock"
    assert result["execution"]["success"] is True
    assert "implementation_summary" in result["output"]
    assert "known_gaps" in result["output"]



def test_runner_build_adapter_payload_includes_routing_config():
    runner = RuntimeRunner()

    payload = runner.build_adapter_payload(
        task={
            "task": {
                "id": "STORY-014",
            },
            "routing": {
                "approval_mode": "full",
                "timeout_seconds": 120,
                "allow_filesystem_write": True,
                "model": "gpt-5-codex",
            },
            "governance": {
                "risk_level": "medium",
                "confidence_score": 90,
            },
        },
        runtime_context={},
        routing_decision={},
        confidence_result={
            "human_validation_required": False,
        },
    )

    routing_config = payload["routing_config"]

    assert routing_config["approval_mode"] == "full"
    assert routing_config["timeout_seconds"] == 120
    assert routing_config["allow_filesystem_write"] is True
    assert routing_config["model"] == "gpt-5-codex"



def test_resolve_approval_mode_filesystem_disabled_forces_suggest():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="full",
        risk_level="low",
        allow_filesystem_write=False,
    )

    assert result == "suggest"



def test_resolve_approval_mode_high_risk_blocks_auto():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="auto",
        risk_level="high",
        allow_filesystem_write=True,
    )

    assert result == "suggest"



def test_resolve_approval_mode_high_risk_blocks_full():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="full",
        risk_level="high",
        allow_filesystem_write=True,
    )

    assert result == "suggest"



def test_resolve_approval_mode_critical_risk_blocks_auto():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="auto",
        risk_level="critical",
        allow_filesystem_write=True,
    )

    assert result == "suggest"



def test_resolve_approval_mode_critical_risk_blocks_full():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="full",
        risk_level="critical",
        allow_filesystem_write=True,
    )

    assert result == "suggest"



def test_resolve_approval_mode_low_risk_suggest_stays_suggest():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="suggest",
        risk_level="low",
        allow_filesystem_write=True,
    )

    assert result == "suggest"



def test_resolve_approval_mode_low_risk_auto_stays_auto():
    adapter = CodexAdapter()

    result = adapter.resolve_approval_mode(
        requested_mode="auto",
        risk_level="low",
        allow_filesystem_write=True,
    )

    assert result == "auto"


@patch("runtime.adapters.codex_adapter.shutil.which")
@patch("runtime.adapters.codex_adapter.subprocess.run")
def test_codex_adapter_successful_invocation(
    mock_run,
    mock_which,
):
    adapter = CodexAdapter()

    mock_which.return_value = "/usr/bin/codex"

    mock_run.return_value = Mock(
        returncode=0,
        stdout=VALID_CODEX_OUTPUT.encode("utf-8"),
        stderr=b"",
    )

    payload = {
        "task": {
            "id": "STORY-001",
            "type": "python-automation",
            "objective": "Build inventory summary CLI",
            "scope": ["Build CLI"],
        },
        "runtime_context": {
            "role": "builder",
            "memory": [
                {
                    "content": "Prefer safe changes.",
                }
            ],
            "stop_conditions": [
                "validation_missing",
            ],
            "required_outputs": [
                "implementation_summary",
            ],
        },
        "routing_config": {
            "approval_mode": "suggest",
            "timeout_seconds": 60,
            "allow_filesystem_write": False,
            "model": "gpt-5",
        },
        "governance": {
            "risk_level": "low",
            "confidence_score": 90,
            "confidence_threshold": 85,
            "human_validation_required": False,
            "required_outputs": [
                "implementation_summary",
            ],
        },
    }

    result = adapter.invoke(payload)

    assert result["execution"]["success"] is True
    assert result["adapter"]["name"] == "codex"
    assert result["adapter"]["approval_mode"] == "suggest"
    assert result["errors"] == []


@patch("runtime.adapters.codex_adapter.shutil.which")
@patch("runtime.adapters.codex_adapter.subprocess.run")
def test_codex_adapter_timeout_handling(
    mock_run,
    mock_which,
):
    adapter = CodexAdapter()

    mock_which.return_value = "/usr/bin/codex"

    mock_run.side_effect = (
        subprocess.TimeoutExpired(
            cmd="codex",
            timeout=60,
        )
    )

    result = adapter.invoke(
        {
            "routing_config": {
                "timeout_seconds": 60,
            },
            "governance": {
                "risk_level": "low",
                "confidence_score": 90,
            },
        }
    )

    assert result["execution"]["success"] is False
    assert "timeout" in result["errors"][0]


@patch("runtime.adapters.codex_adapter.shutil.which")
@patch("runtime.adapters.codex_adapter.subprocess.run")
def test_codex_adapter_malformed_output_handling(
    mock_run,
    mock_which,
):
    adapter = CodexAdapter()

    mock_which.return_value = "/usr/bin/codex"

    mock_run.return_value = Mock(
        returncode=0,
        stdout=b"Incomplete output",
        stderr=b"",
    )

    result = adapter.invoke(
        {
            "routing_config": {
                "timeout_seconds": 60,
            },
            "governance": {
                "risk_level": "low",
                "confidence_score": 90,
            },
        }
    )

    assert result["execution"]["success"] is True

    assert any(
        "malformed_output" in error
        for error in result["errors"]
    )


@patch("runtime.adapters.codex_adapter.shutil.which")
def test_codex_adapter_handles_missing_cli(
    mock_which,
):
    adapter = CodexAdapter()

    mock_which.return_value = None

    result = adapter.invoke(
        {
            "governance": {
                "confidence_score": 90,
            }
        }
    )

    assert result["execution"]["success"] is False

    assert any(
        "adapter_not_available" in error
        for error in result["errors"]
    )



def test_adapter_registry_returns_mock_adapter():
    registry = AdapterRegistry()

    adapter = registry.get("mock")

    assert isinstance(adapter, MockAdapter)



def test_adapter_registry_returns_codex_adapter():
    registry = AdapterRegistry()

    adapter = registry.get("codex")

    assert isinstance(adapter, CodexAdapter)



def test_adapter_registry_rejects_unknown_adapter():
    registry = AdapterRegistry()

    try:
        registry.get("unknown")
    except ValueError as error:
        assert "Unknown adapter" in str(error)
    else:
        raise AssertionError("Expected ValueError for unknown adapter")
