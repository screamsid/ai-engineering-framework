from pathlib import Path


VERSION_FILE = Path(__file__).resolve().parent.parent / "VERSION.md"


def get_framework_version() -> str:
    """Read the canonical framework version from VERSION.md."""

    for line in VERSION_FILE.read_text(
        encoding="utf-8"
    ).splitlines():
        if line.startswith("Current Version:"):
            version = line.split(":", 1)[1].strip()
            return version.removeprefix("v")

    raise ValueError(
        "Current Version not found in VERSION.md"
    )
