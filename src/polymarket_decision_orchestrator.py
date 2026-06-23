from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable


class Decision(str, Enum):
    BLOCKED = "BLOCKED"
    KILL = "KILL"
    HOLD = "HOLD"
    SCOUT = "SCOUT"
    PROMOTE_REVIEW = "PROMOTE_REVIEW"


class EvidenceLayer(str, Enum):
    REPLAY_ONLY = "REPLAY_ONLY"
    SHADOW_WOULD_BUY = "SHADOW_WOULD_BUY"
    LIVE_NO_FILL = "LIVE_NO_FILL"
    LIVE_FILL = "LIVE_FILL"
    CASH_TRUTH = "CASH_TRUTH"


@dataclass(frozen=True)
class CandidateEvidence:
    evidence_layer: EvidenceLayer
    replay_positive: bool = False
    shadow_positive: bool = False
    live_fill_positive: bool = False
    cash_truth_positive: bool = False
    fillability_adjusted_pnl: float | None = None
    max_loss_streak: int | None = None
    kill_switch_active: bool = False
    heartbeat_fresh: bool = True
    human_approval: bool = False
    notes: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class DecisionReport:
    decision: Decision
    confidence: str
    blocking_gates: tuple[str, ...]
    evidence_layer: EvidenceLayer
    next_action: str
    do_not_do: tuple[str, ...]


def _tuple(values: Iterable[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def decide_candidate(evidence: CandidateEvidence) -> DecisionReport:
    blocks: list[str] = []
    do_not_do = [
        "do_not_place_live_orders",
        "do_not_raise_stake",
        "do_not_disable_kill_switch",
    ]

    if evidence.kill_switch_active:
        blocks.append("KILL_SWITCH_ACTIVE")
    if not evidence.heartbeat_fresh:
        blocks.append("RUNTIME_HEARTBEAT_STALE")
    if evidence.fillability_adjusted_pnl is not None and evidence.fillability_adjusted_pnl <= 0:
        blocks.append("FILLABILITY_ADJUSTED_PNL_NOT_POSITIVE")
    if evidence.max_loss_streak is not None and evidence.max_loss_streak >= 5:
        blocks.append("MAX_LOSS_STREAK_TOO_HIGH")

    if blocks:
        return DecisionReport(
            decision=Decision.BLOCKED,
            confidence="HIGH",
            blocking_gates=_tuple(blocks),
            evidence_layer=evidence.evidence_layer,
            next_action="fix_blocking_gates_before_any_promotion",
            do_not_do=_tuple(do_not_do),
        )

    if evidence.evidence_layer == EvidenceLayer.REPLAY_ONLY:
        return DecisionReport(
            decision=Decision.SCOUT if evidence.replay_positive else Decision.KILL,
            confidence="LOW",
            blocking_gates=(),
            evidence_layer=evidence.evidence_layer,
            next_action="run_shadow_evaluation",
            do_not_do=_tuple(do_not_do),
        )

    if evidence.evidence_layer in {EvidenceLayer.SHADOW_WOULD_BUY, EvidenceLayer.LIVE_NO_FILL}:
        if evidence.replay_positive and evidence.shadow_positive:
            return DecisionReport(
                decision=Decision.HOLD,
                confidence="MEDIUM",
                blocking_gates=("LIVE_FILL_OR_CASH_TRUTH_MISSING",),
                evidence_layer=evidence.evidence_layer,
                next_action="collect_fillability_and_cash_truth_evidence",
                do_not_do=_tuple(do_not_do),
            )
        return DecisionReport(
            decision=Decision.KILL,
            confidence="MEDIUM",
            blocking_gates=(),
            evidence_layer=evidence.evidence_layer,
            next_action="archive_candidate_and_search_next_mechanism",
            do_not_do=_tuple(do_not_do),
        )

    if evidence.evidence_layer in {EvidenceLayer.LIVE_FILL, EvidenceLayer.CASH_TRUTH}:
        aligned = (
            evidence.replay_positive
            and evidence.shadow_positive
            and evidence.live_fill_positive
            and evidence.cash_truth_positive
        )
        if aligned and evidence.human_approval:
            return DecisionReport(
                decision=Decision.PROMOTE_REVIEW,
                confidence="HIGH",
                blocking_gates=(),
                evidence_layer=evidence.evidence_layer,
                next_action="human_review_of_sizing_and_execution_plan",
                do_not_do=("do_not_auto_execute",),
            )
        if aligned:
            return DecisionReport(
                decision=Decision.HOLD,
                confidence="HIGH",
                blocking_gates=("HUMAN_APPROVAL_MISSING",),
                evidence_layer=evidence.evidence_layer,
                next_action="request_human_approval",
                do_not_do=_tuple(do_not_do),
            )
        return DecisionReport(
            decision=Decision.KILL,
            confidence="HIGH",
            blocking_gates=(),
            evidence_layer=evidence.evidence_layer,
            next_action="do_not_promote_disagreed_evidence",
            do_not_do=_tuple(do_not_do),
        )

    return DecisionReport(
        decision=Decision.BLOCKED,
        confidence="LOW",
        blocking_gates=("UNKNOWN_EVIDENCE_LAYER",),
        evidence_layer=evidence.evidence_layer,
        next_action="provide_valid_evidence_layer",
        do_not_do=_tuple(do_not_do),
    )

