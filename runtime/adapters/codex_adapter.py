import shutil
import subprocess
import time

from runtime.adapters.base_adapter import BaseAdapter


REQUIRED_OUTPUT_SECTIONS = {
    "implementation_summary": "## Implementation Summary",
    "validation_summary": "## Validation Summary",
    "confidence_gate": "## Confidence Gate",
    "known_gaps": "## Known Gaps",
    "handoff": "## Handoff",
}

APPROVAL_MODE_FLAGS = {
    "suggest": "--suggest",
    "auto": "--auto-edit",
    "full": "--full-auto",
}


class CodexAdapter(BaseAdapter):
    """Codex CLI execution adapter.

    Prototype boundary:
    - invokes the local Codex CLI only
    - returns structured adapter results
    - does not use the Codex API directly
    - remains tested with mocked subprocess execution until validated against a real CLI
    """

    adapter_name = "codex"

    def invoke(self, runtime_payload: dict) -> dict:
        started_at = time.monotonic()

        routing_config = runtime_payload.get(
            "routing_config",
            {},
        )
        governance = runtime_payload.get(
            "governance",
            {},
        )

        approval_mode = self.resolve_approval_mode(
            requested_mode=routing_config.get(
                "approval_mode",
                "suggest",
            ),
            risk_level=governance.get(
                "risk_level",
                "low",
            ),
            allow_filesystem_write=routing_config.get(
                "allow_filesystem_write",
                False,
            ),
        )

        timeout_seconds = routing_config.get(
            "timeout_seconds",
            300,
        )
        model = routing_config.get(
            "model",
            "gpt-5",
        )

        prompt = self.build_prompt(runtime_payload)

        codex_path = shutil.which("codex")

        if codex_path is None:
            return self.build_error_result(
                error="adapter_not_available: Codex CLI not found in PATH",
                started_at=started_at,
                governance=governance,
                approval_mode=approval_mode,
            )

        command = [
            codex_path,
            APPROVAL_MODE_FLAGS[approval_mode],
            "-m",
            model,
            prompt,
        ]

        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                timeout=timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return self.build_error_result(
                error=(
                    "timeout: Codex CLI exceeded "
                    f"{timeout_seconds} seconds"
                ),
                started_at=started_at,
                governance=governance,
                approval_mode=approval_mode,
            )

        stdout = self.decode_output(completed.stdout)
        stderr = self.decode_output(completed.stderr)

        parsed_output = self.parse_output(stdout)

        errors = []

        if completed.returncode != 0:
            errors.append(
                "non_zero_exit: Codex CLI exited with "
                f"code {completed.returncode}"
            )

        if stderr:
            errors.append(f"stderr: {stderr}")

        missing_sections = [
            section
            for section, heading in REQUIRED_OUTPUT_SECTIONS.items()
            if heading not in stdout
        ]

        if missing_sections:
            errors.append(
                "malformed_output: Missing required sections: "
                + ", ".join(missing_sections)
            )

        human_checkpoint = governance.get(
            "human_validation_required",
            False,
        )

        if human_checkpoint:
            parsed_output["handoff"] = (
                parsed_output.get("handoff")
                or "Human validation required before completion."
            )

        return {
            "adapter": {
                "name": self.adapter_name,
                "version": "0.1.0",
                "approval_mode": approval_mode,
                "model": model,
            },
            "execution": {
                "success": completed.returncode == 0,
                "execution_time_ms": self.elapsed_ms(
                    started_at
                ),
                "token_estimate": 0,
            },
            "output": parsed_output,
            "governance": {
                "confidence_score": governance.get(
                    "confidence_score",
                    0,
                ),
                "human_validation_required": human_checkpoint,
                "human_checkpoint": (
                    "Human validation required before completion."
                    if human_checkpoint
                    else None
                ),
            },
            "errors": errors,
        }

    def resolve_approval_mode(
        self,
        requested_mode: str,
        risk_level: str,
        allow_filesystem_write: bool,
    ) -> str:
        mode = requested_mode

        if mode not in APPROVAL_MODE_FLAGS:
            mode = "suggest"

        if not allow_filesystem_write:
            return "suggest"

        if risk_level in ["high", "critical"] and mode == "auto":
            return "suggest"

        return mode

    def build_prompt(self, runtime_payload: dict) -> str:
        task = runtime_payload.get("task", {})
        context = runtime_payload.get(
            "runtime_context",
            {},
        )
        governance = runtime_payload.get(
            "governance",
            {},
        )
        routing_config = runtime_payload.get(
            "routing_config",
            {},
        )

        memory_items = context.get("memory", [])
        memory_text = "\n".join(
            f"- {item.get('content', item)}"
            if isinstance(item, dict)
            else f"- {item}"
            for item in memory_items
        )

        required_outputs = governance.get(
            "required_outputs",
            context.get("required_outputs", []),
        )
        stop_conditions = context.get(
            "stop_conditions",
            [],
        )

        return "\n".join(
            [
                "You are operating inside the AI Engineering Framework.",
                "Follow the runtime governance constraints exactly.",
                "",
                f"Role: {context.get('role', 'builder')}",
                f"Task ID: {task.get('id')}",
                f"Task Type: {task.get('type')}",
                f"Objective: {task.get('objective')}",
                "",
                "Scope:",
                *[
                    f"- {item}"
                    for item in task.get("scope", [])
                ],
                "",
                "Governance:",
                f"- Risk level: {governance.get('risk_level')}",
                f"- Confidence threshold: {governance.get('confidence_threshold')}",
                "- Filesystem writes allowed: "
                f"{routing_config.get('allow_filesystem_write', False)}",
                "",
                "Required output sections:",
                *[
                    f"- {section}"
                    for section in required_outputs
                ],
                "",
                "Stop conditions:",
                *[
                    f"- {condition}"
                    for condition in stop_conditions
                ],
                "",
                "Relevant memory:",
                memory_text or "- None",
                "",
                "Return your response using these markdown headings exactly:",
                "## Implementation Summary",
                "## Validation Summary",
                "## Confidence Gate",
                "## Known Gaps",
                "## Handoff",
            ]
        )

    def parse_output(self, stdout: str) -> dict:
        return {
            "implementation_summary": self.extract_section(
                stdout,
                "## Implementation Summary",
            ),
            "validation_summary": self.extract_section(
                stdout,
                "## Validation Summary",
            ),
            "confidence_gate": self.extract_section(
                stdout,
                "## Confidence Gate",
            ),
            "known_gaps": self.extract_known_gaps(stdout),
            "handoff": self.extract_section(
                stdout,
                "## Handoff",
            ),
        }

    def extract_section(
        self,
        text: str,
        heading: str,
    ) -> str:
        if heading not in text:
            return ""

        section = text.split(heading, 1)[1]

        for next_heading in REQUIRED_OUTPUT_SECTIONS.values():
            if next_heading == heading:
                continue
            marker = f"\n{next_heading}"
            if marker in section:
                section = section.split(marker, 1)[0]

        return section.strip()

    def extract_known_gaps(self, text: str) -> list:
        section = self.extract_section(
            text,
            "## Known Gaps",
        )

        if not section:
            return []

        gaps = []

        for line in section.splitlines():
            cleaned = line.strip()
            if cleaned.startswith("- "):
                gaps.append(cleaned[2:])

        return gaps or [section]

    def build_error_result(
        self,
        error: str,
        started_at: float,
        governance: dict,
        approval_mode: str,
    ) -> dict:
        return {
            "adapter": {
                "name": self.adapter_name,
                "version": "0.1.0",
                "approval_mode": approval_mode,
            },
            "execution": {
                "success": False,
                "execution_time_ms": self.elapsed_ms(
                    started_at
                ),
                "token_estimate": 0,
            },
            "output": {
                "implementation_summary": "",
                "validation_summary": "",
                "confidence_gate": "",
                "known_gaps": [],
                "handoff": "",
            },
            "governance": {
                "confidence_score": governance.get(
                    "confidence_score",
                    0,
                ),
                "human_validation_required": governance.get(
                    "human_validation_required",
                    False,
                ),
            },
            "errors": [error],
        }

    def decode_output(self, output: bytes | str) -> str:
        if isinstance(output, str):
            return output.strip()

        try:
            return output.decode("utf-8").strip()
        except UnicodeDecodeError:
            return output.decode("latin-1").strip()

    def elapsed_ms(self, started_at: float) -> int:
        return int((time.monotonic() - started_at) * 1000)
