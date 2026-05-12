from pathlib import Path
import yaml


class CalibrationEngine:
    """Very small adaptive confidence adjustment engine."""

    def __init__(
        self,
        policy_path: str = "runtime/calibration/calibration-policy.yaml",
    ):
        policy_file = Path(policy_path)

        with open(policy_file, "r", encoding="utf-8") as handle:
            self.policy = yaml.safe_load(handle)[
                "calibration_policy"
            ]

    def adjust(
        self,
        original_confidence: int,
        validation_result: str,
    ) -> dict:
        adjusted_confidence = original_confidence

        if validation_result == "rejected":
            adjusted_confidence = max(
                original_confidence
                + self.policy["rejected_delta"],
                0,
            )

        elif validation_result == "corrected":
            adjusted_confidence = max(
                original_confidence
                + self.policy["corrected_delta"],
                0,
            )

        elif validation_result == "approved":
            adjusted_confidence = min(
                original_confidence
                + self.policy["approved_delta"],
                100,
            )

        return {
            "original_confidence": original_confidence,
            "validation_result": validation_result,
            "adjusted_confidence": adjusted_confidence,
            "policy_used": self.policy,
        }
