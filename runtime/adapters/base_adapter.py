class BaseAdapter:
    """Base execution adapter interface.

    Adapters isolate vendor-specific execution behaviour from the governance runtime.

    The runtime should only interact with standardised execution contracts.
    """

    adapter_name = "base"

    def invoke(self, runtime_payload: dict) -> dict:
        """Execute runtime payload and return standardised adapter result."""
        raise NotImplementedError(
            "Adapters must implement invoke()"
        )
