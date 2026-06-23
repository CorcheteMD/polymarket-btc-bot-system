# Skill System

This folder contains the public-safe skill and orchestrator layer extracted from the private bot workspace.

The skills are included so another engineer can continue the architecture without needing private credentials, raw datasets, wallets, VPS details, or live execution code.

## Recommended Route

```text
polymarket-system-orchestrator
  -> polymarket-market-discovery
  -> polymarket-ws-streaming
  -> polymarket-historical-archive
  -> clob-microstructure-analysis
  -> forecast-calibration-engine
  -> signal-generation-anomaly
  -> risk-management-gate
  -> order-execution-compliance
```

For the profitability and evidence loop:

```text
trading-success-harness
  -> hb-profitability-orchestrator
  -> hb-dataset-contract-freezer
  -> hb-overfit-kill-battery
  -> shadow-informativeness-auditor
  -> hb-live-cash-truth-pnl
  -> hb-promotion-war-room
```

For harness and operations safety:

```text
bot-harness-architect
  -> bot-agent-shield
  -> bot-eval-harness
  -> bot-status-snapshot
  -> bot-session-memory
  -> botctl-control-plane
```

## Public-Safe Boundary

These skills may describe safety gates, evidence contracts, and orchestration rules. They must not be interpreted as permission to trade live.

This public repo excludes:

- credentials and keys
- raw data
- live endpoints
- VPS details
- wallet lists
- private thresholds
- executable order-placement code

## Skills Included

### Polymarket Core

- `polymarket-system-orchestrator`
- `polymarket-market-discovery`
- `polymarket-ws-streaming`
- `polymarket-historical-archive`
- `clob-microstructure-analysis`
- `forecast-calibration-engine`
- `market-research-intelligence`
- `signal-generation-anomaly`
- `risk-management-gate`
- `order-execution-compliance`
- `polymarket-debugger`

### Profitability Harness

- `trading-success-harness`
- `hb-profitability-orchestrator`
- `hb-dataset-contract-freezer`
- `hb-overfit-kill-battery`
- `hb-live-cash-truth-pnl`
- `hb-promotion-war-room`
- `hb-research-tape-architect`
- `shadow-informativeness-auditor`

### Bot Harness

- `bot-harness-architect`
- `bot-agent-shield`
- `bot-eval-harness`
- `bot-status-snapshot`
- `bot-session-memory`
- `botctl-control-plane`
- `subagent-handoff-protocol`
- `ecc-extraction-lab`
- `vps-live-safety-ops`

### Quality System

- `universal-quality-orchestrator`
- `quality-context-reader`
- `quality-rubric-builder`
- `quality-evidence-mapper`
- `quality-evidence-scorer`
- `quality-red-team-auditor`
- `quality-root-cause-analyst`
- `quality-verdict-synthesizer`
- `quality-improvement-planner`
- `quality-rescore-validator`

