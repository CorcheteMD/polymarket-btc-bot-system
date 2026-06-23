import unittest

from src.polymarket_decision_orchestrator import (
    CandidateEvidence,
    Decision,
    EvidenceLayer,
    decide_candidate,
)


class DecisionOrchestratorTest(unittest.TestCase):
    def test_replay_only_cannot_promote(self) -> None:
        report = decide_candidate(
            CandidateEvidence(
                evidence_layer=EvidenceLayer.REPLAY_ONLY,
                replay_positive=True,
            )
        )
        self.assertEqual(report.decision, Decision.SCOUT)
        self.assertIn("do_not_place_live_orders", report.do_not_do)

    def test_negative_fillability_blocks(self) -> None:
        report = decide_candidate(
            CandidateEvidence(
                evidence_layer=EvidenceLayer.SHADOW_WOULD_BUY,
                replay_positive=True,
                shadow_positive=True,
                fillability_adjusted_pnl=-0.01,
            )
        )
        self.assertEqual(report.decision, Decision.BLOCKED)
        self.assertIn("FILLABILITY_ADJUSTED_PNL_NOT_POSITIVE", report.blocking_gates)

    def test_aligned_cash_truth_without_human_approval_holds(self) -> None:
        report = decide_candidate(
            CandidateEvidence(
                evidence_layer=EvidenceLayer.CASH_TRUTH,
                replay_positive=True,
                shadow_positive=True,
                live_fill_positive=True,
                cash_truth_positive=True,
                human_approval=False,
            )
        )
        self.assertEqual(report.decision, Decision.HOLD)
        self.assertIn("HUMAN_APPROVAL_MISSING", report.blocking_gates)

    def test_aligned_cash_truth_with_human_approval_promotes_review_only(self) -> None:
        report = decide_candidate(
            CandidateEvidence(
                evidence_layer=EvidenceLayer.CASH_TRUTH,
                replay_positive=True,
                shadow_positive=True,
                live_fill_positive=True,
                cash_truth_positive=True,
                human_approval=True,
            )
        )
        self.assertEqual(report.decision, Decision.PROMOTE_REVIEW)
        self.assertIn("do_not_auto_execute", report.do_not_do)


if __name__ == "__main__":
    unittest.main()

