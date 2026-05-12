from runtime.adapters.mock_adapter import MockAdapter
from runtime.adapters.registry import AdapterRegistry


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


def test_adapter_registry_returns_mock_adapter():
    registry = AdapterRegistry()

    adapter = registry.get("mock")

    assert isinstance(adapter, MockAdapter)


def test_adapter_registry_rejects_unknown_adapter():
    registry = AdapterRegistry()

    try:
        registry.get("unknown")
    except ValueError as error:
        assert "Unknown adapter" in str(error)
    else:
        raise AssertionError("Expected ValueError for unknown adapter")
