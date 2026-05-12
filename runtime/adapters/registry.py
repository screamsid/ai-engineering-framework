from runtime.adapters.mock_adapter import MockAdapter
from runtime.adapters.codex_adapter import CodexAdapter
from runtime.adapters.claude_code_adapter import ClaudeCodeAdapter
from runtime.adapters.antigravity_adapter import AntigravityAdapter


class AdapterRegistry:
    """Runtime adapter registry.

    Keeps runtime governance isolated from provider-specific adapter logic.
    """

    def __init__(self):
        self.adapters = {
            "mock": MockAdapter,
            "codex": CodexAdapter,
            "claude-code": ClaudeCodeAdapter,
            "antigravity": AntigravityAdapter,
        }

    def get(self, adapter_name: str):
        adapter_class = self.adapters.get(adapter_name)

        if adapter_class is None:
            raise ValueError(
                f"Unknown adapter: {adapter_name}"
            )

        return adapter_class()
