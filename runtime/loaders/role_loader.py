from pathlib import Path
import yaml


class RoleLoader:
    """Load runtime role cards."""

    def __init__(self, rules_path: str = "runtime/rules"):
        self.rules_path = Path(rules_path)

    def load(self, role_name: str) -> dict:
        role_file = self.rules_path / f"{role_name}.rule-card.yaml"

        if not role_file.exists():
            raise FileNotFoundError(
                f"Role card not found: {role_file}"
            )

        with open(role_file, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)

        return data.get("role_card", {})
