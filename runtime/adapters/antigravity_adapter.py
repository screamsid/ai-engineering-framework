from runtime.adapters.base_adapter import BaseAdapter


class AntigravityAdapter(BaseAdapter):
    """Antigravity orchestration adapter scaffold.

    Future implementation areas:
    - orchestration integration
    - task coordination
    - multi-agent routing
    - runtime telemetry
    - adapter result normalisation
    """

    adapter_name = "antigravity"

    def invoke(self, runtime_payload: dict) -> dict:
        raise NotImplementedError(
            "Antigravity adapter execution not implemented yet."
        )
