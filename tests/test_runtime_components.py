from runtime.gates.confidence_gate import ConfidenceGate
from runtime.calibration.calibration_engine import CalibrationEngine
from runtime.router.router import RuntimeRouter
from runtime.runner import RuntimeRunner


THRESHOLDS = {
    "low": 85,
    "medium": 90,
    "high": 95,
}


def test_confidence_gate_approves_when_score_meets_threshold():
    gate = ConfidenceGate()

    result = gate.evaluate(
        confidence_score=90,
        risk_level="medium",
        thresholds=THRESHOLDS,
    )

    assert result["approved"] is True
    assert result["human_validation_required"] is False


def test_confidence_gate_requires_human_for_low_score():
    gate = ConfidenceGate()

    result = gate.evaluate(
        confidence_score=80,
        risk_level="medium",
        thresholds=THRESHOLDS,
    )

    assert result["approved"] is False
    assert result["human_validation_required"] is True


def test_confidence_gate_requires_human_for_critical_risk():
    gate = ConfidenceGate()

    result = gate.evaluate(
        confidence_score=100,
        risk_level="critical",
        thresholds=THRESHOLDS,
    )

    assert result["approved"] is False
    assert result["human_validation_required"] is True
    assert result["required_score"] == "human-review-required"


def test_calibration_engine_adjusts_rejected_confidence_down():
    engine = CalibrationEngine()

    result = engine.adjust(
        original_confidence=90,
        validation_result="rejected",
    )

    assert result["adjusted_confidence"] < 90


def test_calibration_engine_adjusts_approved_confidence_up():
    engine = CalibrationEngine()

    result = engine.adjust(
        original_confidence=90,
        validation_result="approved",
    )

    assert result["adjusted_confidence"] > 90


def test_router_assigns_builder_for_python_automation():
    router = RuntimeRouter()

    task = {
        "task": {
            "type": "python-automation",
        },
        "runtime": {
            "risk_level": "low",
        },
    }

    decision = router.route(task)

    assert decision["assignment"]["role"] == "builder"
    assert decision["assignment"]["preferred_agent"] == "codex"


def test_router_requires_reviews_for_high_risk():
    router = RuntimeRouter()

    task = {
        "task": {
            "type": "infra-automation",
        },
        "runtime": {
            "risk_level": "high",
        },
    }

    decision = router.route(task)

    assert decision["governance"]["reviewer_required"] is True
    assert decision["governance"]["security_review_required"] is True


def test_runtime_runner_returns_runtime_result():
    runner = RuntimeRunner()

    result = runner.run("examples/runtime-task.yaml")

    assert "runtime_result" in result
    assert "human_output" in result
    assert "prototype_limits" in result["runtime_result"]
