from pathlib import Path


class SkillLoader:
    """Load available runtime skill packs."""

    def __init__(self, skills_path: str = "skills"):
        self.skills_path = Path(skills_path)

    def load(self, skill_name: str) -> dict:
        skill_file = self.skills_path / skill_name / "SKILL.md"

        if not skill_file.exists():
            raise FileNotFoundError(
                f"Skill pack not found: {skill_file}"
            )

        return {
            "name": skill_name,
            "path": str(skill_file),
            "content": skill_file.read_text(encoding="utf-8"),
        }
