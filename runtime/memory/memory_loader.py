class MemoryLoader:
    """Select relevant memory items for runtime context.

    This loader is intentionally simple and deterministic for v0.3.
    Future versions may add scoring, decay, confidence weighting, and
    domain trust integration.
    """

    def __init__(self, memory_items: list | None = None):
        self.memory_items = memory_items or []

    def load_relevant(
        self,
        task_type: str,
        risk_level: str,
        limit: int = 5,
    ) -> list:
        relevant = []

        for item in self.memory_items:
            applies_to = item.get("applies_to", [])
            risk_scope = item.get("risk_scope", [])

            task_match = (
                not applies_to
                or task_type in applies_to
            )

            risk_match = (
                not risk_scope
                or risk_level in risk_scope
            )

            if task_match and risk_match:
                relevant.append(item)

        return relevant[:limit]
