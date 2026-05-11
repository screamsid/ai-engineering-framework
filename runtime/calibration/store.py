from pathlib import Path
import json


class CalibrationStore:
    """Simple JSON calibration record store."""

    def __init__(
        self,
        store_path: str = "runtime_state/calibration_records.json",
    ):
        self.store_path = Path(store_path)
        self.store_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(self, record: dict) -> None:
        records = []

        if self.store_path.exists():
            records = json.loads(
                self.store_path.read_text(encoding="utf-8")
            )

        records.append(record)

        self.store_path.write_text(
            json.dumps(records, indent=2),
            encoding="utf-8",
        )
