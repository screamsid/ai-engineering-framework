class CalibrationEngine:
    """Very small adaptive confidence adjustment engine."""

    def adjust(
        self,
        original_confidence: int,
        validation_result: str,
    ) -> dict:
        adjusted_confidence = original_confidence

        if validation_result == "rejected":
            adjusted_confidence = max(
                original_confidence - 15,
                0,
            )

        elif validation_result == "corrected":
            adjusted_confidence = max(
                original_confidence - 5,
                0,
            )

        elif validation_result == "approved":
            adjusted_confidence = min(
                original_confidence + 2,
                100,
            )

        return {
            "original_confidence": original_confidence,
            "validation_result": validation_result,
            "adjusted_confidence": adjusted_confidence,
        }
