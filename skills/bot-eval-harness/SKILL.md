---
name: bot-eval-harness
description: Use to design or run a read-only evaluation harness for the bot: tests, replay, OOS, walk-forward, calibration, fill realism, risk gates, and promotion readiness. Does not tune strategies or execute trades.
---

# Bot Eval Harness

## Mission

Turn evidence into a repeatable readiness decision. The eval harness answers: what was tested, against what data, with what gates, and what remains unproven.

## Inputs

- Candidate strategy or system change.
- Test suite.
- Replay/paper/live reports.
- Dataset manifest.
- Microstructure/fill realism report.
- Risk limits.

## Workflow

1. Identify evidence purpose: discovery, replay, shadow, paper, live.
2. Verify dataset contract with `hb-dataset-contract-freezer`.
3. Run or request deterministic tests.
4. Apply overfit checks with `hb-overfit-kill-battery`.
5. Check calibration and fill realism.
6. Produce readiness verdict.

## Output

- `BLOCKED_MISSING_EVIDENCE`
- `DISCOVERY_ONLY`
- `SCOUT_READY`
- `PAPER_READY`
- `PROMOTION_REVIEW_READY`
- `LIVE_BLOCKED`

## Hard Rules

- A pretty backtest is not readiness.
- Remove-best checks and temporal block checks must be explicit.
- Promotion requires risk gate and human approval.

