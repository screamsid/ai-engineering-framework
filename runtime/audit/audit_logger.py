from pathlib import Path
from datetime import datetime, UTC


class AuditLogger:
    """Simple runtime audit logger."""

    def __init__(
        self,
        log_path: str = "runtime_state/audit.log",
    ):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(self, event: str) -> None:
        timestamp = datetime.now(UTC).isoformat()

        with open(self.log_path, "a", encoding="utf-8") as handle:
            handle.write(
                f"[{timestamp}] {event}\n"
            )
