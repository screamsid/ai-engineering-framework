class ContextAssembler:
    """Assemble minimal runtime context for agent execution."""

    def assemble(
        self,
        role_card: dict,
        skills: list,
        task: dict,
        memory_items: list | None = None,
    ) -> dict:
        return {
            "task": task,
            "role": role_card.get("role"),
            "purpose": role_card.get("purpose", []),
            "required_outputs": role_card.get(
                "required_outputs", []
            ),
            "stop_conditions": role_card.get(
                "stop_conditions", []
            ),
            "confidence": role_card.get("confidence", {}),
            "skills": [
                skill.get("name")
                for skill in skills
            ],
            "memory": memory_items or [],
        }
