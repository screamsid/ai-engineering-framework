class ContextCompiler:
    """Compile minimal runtime context for adapter execution.

    The compiler keeps execution payloads small by selecting only the context
    required for the current task, role, risk, and adapter.
    """

    def compile(self, runtime_context: dict) -> dict:
        return {
            "role": runtime_context.get("role"),
            "task": runtime_context.get("task", {}).get("task", {}),
            "required_outputs": runtime_context.get(
                "required_outputs", []
            ),
            "stop_conditions": runtime_context.get(
                "stop_conditions", []
            ),
            "confidence": runtime_context.get("confidence", {}),
            "skills": runtime_context.get("skills", []),
            "memory": runtime_context.get("memory", []),
        }
