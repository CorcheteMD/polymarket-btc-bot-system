from __future__ import annotations

from src.polymarket_decision_orchestrator import DecisionReport


def render_decision_report(report: DecisionReport) -> str:
    gates = ", ".join(report.blocking_gates) if report.blocking_gates else "none"
    guardrails = "\n".join(f"- `{item}`" for item in report.do_not_do)
    return "\n".join(
        [
            "# Candidate Decision Report",
            "",
            f"- Decision: `{report.decision.value}`",
            f"- Confidence: `{report.confidence}`",
            f"- Evidence layer: `{report.evidence_layer.value}`",
            f"- Blocking gates: {gates}",
            f"- Next action: {report.next_action}",
            "",
            "## Do Not Do",
            "",
            guardrails,
            "",
        ]
    )

