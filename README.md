# Polymarket BTC Bot System

Case-study repository for a BTC/Polymarket trading-bot architecture: market discovery, WebSocket data capture, dry-run evaluation, profitability gates, and execution safety. This public version is intentionally sanitized. It shows the system design and decision contracts, not private keys, datasets, live endpoints, wallet data, or proprietary edge parameters.

## What This Shows

- A layered architecture for a prediction-market bot.
- How I separate market discovery, streaming, signal research, risk review, and execution.
- A deterministic decision orchestrator that blocks live actions unless evidence and gates agree.
- Public data contracts for market ticks, microstructure features, and fillability checks.
- Public lessons from the execution-feasibility audit: implied price is not executable price.
- A trade lifecycle scaffold with idempotent close and restart-recovery behavior.
- A continuation roadmap for another engineer to extend the safe scaffold.
- The public-safe skill/orchestrator layer used to route discovery, streaming, research, risk, quality, and promotion review.
- A publication-safe example for portfolio review, CORFO-style technical credibility, and LinkedIn storytelling.

## What This Does Not Include

- No `.env`, private keys, VPS IPs, wallets, Telegram tokens, or exchange credentials.
- No raw Polymarket datasets, logs, SQLite ledgers, model pickles, or backtest artifacts.
- No live trading client and no code that places orders.
- No proprietary strategy thresholds or copy-paste edge.

## Architecture

```text
market discovery
  -> websocket archive
  -> microstructure analysis
  -> forecast / signal candidate
  -> risk gate
  -> human approval
  -> execution compliance
```

The important rule is simple: no component should both create a signal and execute it. Execution must be downstream of risk approval and human review.

## Repository Structure

```text
docs/
  architecture.md
  backtesting-data-requirements.md
  backtest-methodology.md
  bug-prevention-methodology.md
  continuation-guide.md
  data-contract.md
  execution-feasibility-lessons.md
  forensic-audit-playbook.md
  private-exclusion-map.md
  private-source-inventory-before-deletion.md
  risk-gates.md
  roadmap.md
  sanitization-report.md
  system-map.md
  testing-strategy.md
  trade-manager-design.md
examples/
  candidate_evidence.json
  synthetic_ticks.jsonl
skills/
  README.md
  <skill-name>/SKILL.md
src/
  contracts.py
  backtesting_schema.py
  polymarket_decision_orchestrator.py
  reporting.py
  trade_lifecycle.py
tests/
  test_backtesting_schema.py
  test_contracts.py
  test_polymarket_decision_orchestrator.py
  test_trade_lifecycle.py
```

## Quick Start

```bash
python -m unittest discover -s tests
```

## Decision States

- `BLOCKED`: required evidence is missing or runtime safety is uncertain.
- `KILL`: evidence falsifies the candidate.
- `HOLD`: not enough forward evidence yet.
- `SCOUT`: keep researching without promotion.
- `PROMOTE_REVIEW`: ready for human review, not automatic live trading.

## Safety Note

This repository is not financial advice and is not a trading system ready for live use. It is a sanitized engineering artifact that demonstrates architecture, risk controls, and decision discipline.

## Continue The Work

Start with `docs/continuation-guide.md`. The public path is:

```text
contract -> synthetic fixture -> deterministic test -> implementation
```

Private adapters, live execution, and strategy parameters belong outside this public repo.

For the highest-value engineering lesson, read `docs/execution-feasibility-lessons.md` before touching execution logic.

For builders who want to collect their own data, read `docs/backtesting-data-requirements.md`.
