from runtime.adapters.base_adapter import BaseAdapter


class CodexAdapter(BaseAdapter):
    """Codex execution adapter scaffold.

    Future implementation areas:
    - Codex CLI invocation
    - approval mode handling
    - filesystem sandbox control
    - execution telemetry
    - timeout handling
    - adapter result normalisation
    """

    adapter_name = "codex"

    def invoke(self, runtime_payload: dict) -> dict:
        raise NotImplementedError(
            "Codex adapter execution not implemented yet."
        )
