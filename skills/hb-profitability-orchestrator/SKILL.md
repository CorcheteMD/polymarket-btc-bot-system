---
name: hb-profitability-orchestrator
description: Use when coordinating HB Polymarket bot research, replay, shadow, cash-truth, promotion review, runtime safety, or multi-agent profitability work. It routes work to the correct skills/subagents and blocks live changes unless explicitly approved.
---

# HB Profitability Orchestrator

Mission: coordinate the HB bot profitability loop without self-deception.

## Operating Mode

- Default autonomy is `PROPOSE_ONLY`.
- Never lift halt, change stake, enable real orders, or deploy live changes.
- Produce `KILL`, `HOLD`, `SCOUT`, `PROMOTE_REVIEW`, or `BLOCKED`.
- Default to proactive recommendations: propose the next highest-value paths, shadows, kill decisions, and validation gates instead of waiting for the user to choose commands.
- Use `scripts/hb_profit_orchestrator.py recommend` for the main profitability roadmap.
- Use `scripts/hb_profit_orchestrator.py` for deterministic status, truth, shadow-report, promotion-review, skill-gap, and recommendation checks.

## Routing

1. Data/source ambiguity -> `hb-dataset-contract-freezer`.
2. Replay candidate -> `hb-overfit-kill-battery`.
3. Shadow slate -> `shadow-strategy-lab` then `shadow-informativeness-auditor`.
4. Live/context/ledger reconciliation -> `live-truth-reconciler` and `hb-live-cash-truth-pnl`.
5. Latency/no-fill issue -> `hb-latency-forensics`.
6. Promotion decision -> `hb-promotion-war-room`, `polymarket-profitability-gate`, then `mythos-v3`.
7. Remote/VPS action -> `vps-live-safety-ops` first.

## Proactive Roadmap Mode

When the user asks what to do next, run `recommend`.

The output must include:

- best current candidate
- shadows to keep
- shadows to kill
- challengers to add
- ranked paths by expected value
- evidence still missing before live
- explicit `do_not_do` guardrails

Prefer one-dimensional challengers around a winning mechanism. Do not combine many new filters in one challenger unless a prior forward result justifies it.

## Persistent Memory Protocol

Before each new profitability iteration:

1. Read `vault/research/HB_PROFITABILITY_OPERATING_MEMORY.md` if it exists.
2. Read the latest `vault/data/hb_profit_orchestrator_recommend_*.json`.
3. Do not re-litigate settled facts unless new evidence invalidates them.
4. After the iteration, update the memory file with:
   - current decision
   - artifacts used
   - facts confirmed
   - facts falsified
   - next highest-value actions
   - guardrails that still apply

Append machine-readable decisions to `vault/data/MYTHOS_DECISION_LOG.jsonl` or `vault/data/HB_PROFITABILITY_ITERATION_LOG.jsonl`.

## Required Decision Contract

Every subagent output must include:

- `verdict`
- `confidence`
- `blocking_gates`
- `artifacts`
- `next_action`
- `do_not_do`
- evidence layer used: `REPLAY_ONLY`, `SHADOW_WOULD_BUY`, `LIVE_NO_FILL`, `LIVE_FILL`, or `CASH_TRUTH`

## Hard Gates

- Do not promote if replay/shadow/live truth disagree.
- Do not count shadow or blocked rows as real fills.
- Do not promote direct shadows using stale `limit_price=1.0`; use observed direct ask.
- Do not run full-root research scans on the live VPS.
- Do not replace a working baseline with a modified variant before forward evidence.
