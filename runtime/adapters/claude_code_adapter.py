from runtime.adapters.base_adapter import BaseAdapter


class ClaudeCodeAdapter(BaseAdapter):
    """Claude Code execution adapter scaffold.

    Future implementation areas:
    - Claude Code CLI invocation
    - permission handling
    - execution telemetry
    - adapter result normalisation
    - timeout handling
    """

    adapter_name = "claude-code"

    def invoke(self, runtime_payload: dict) -> dict:
        raise NotImplementedError(
            "Claude Code adapter execution not implemented yet."
        )
