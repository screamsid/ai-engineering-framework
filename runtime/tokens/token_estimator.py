class TokenEstimator:
    """Lightweight token estimator for runtime context sizing.

    This is an approximation only.
    It exists to identify oversized payloads before adapter execution.
    """

    def estimate_text(self, text: str) -> int:
        if not text:
            return 0

        # Rough approximation: 1 token per 4 characters.
        return max(1, len(text) // 4)

    def estimate_payload(self, payload: dict) -> dict:
        payload_text = str(payload)
        estimated_tokens = self.estimate_text(payload_text)

        return {
            "estimated_tokens": estimated_tokens,
            "method": "rough_char_div_4",
            "warning": estimated_tokens > 4000,
        }
