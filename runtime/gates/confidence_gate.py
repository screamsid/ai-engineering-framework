class ConfidenceGate:
    """Apply confidence thresholds based on risk level."""

    def evaluate(
        self,
        confidence_score: int,
        risk_level: str,
        thresholds: dict,
    ) -> dict:
        if risk_level == "critical":
            return {
                "approved": False,
                "confidence_score": confidence_score,
                "required_score": "human-review-required",
                "risk_level": risk_level,
                "human_validation_required": True,
            }

        required_score = thresholds.get(risk_level)

        if required_score is None:
            raise ValueError(
                f"Unknown risk level: {risk_level}"
            )

        approved = confidence_score >= required_score

        return {
            "approved": approved,
            "confidence_score": confidence_score,
            "required_score": required_score,
            "risk_level": risk_level,
            "human_validation_required": not approved,
        }
