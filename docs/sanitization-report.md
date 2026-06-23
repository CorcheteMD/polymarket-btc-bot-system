# Sanitization Report

Source inspected: `C:\Users\matia\Downloads\new bot btc`

Prepared: 2026-06-23 11:32 CLT

## Publication Decision

Verdict: `PUBLICAR CON CAMBIOS`

The raw workspace must not be published directly. It contains a local Git history, environment files, private key files, runtime logs, large CSV datasets, model artifacts, SQLite/runtime state, VPS references, and live-bot operational notes.

## Red Items Removed

| Item | Status | Action |
|---|---|---|
| `.env`, `.env.*` | Removed | Never publish |
| `*.pem`, private keys | Removed | Never publish |
| VPS IPs and SSH/SCP commands | Removed | Replace with placeholders in public docs |
| Raw CSV market data | Removed | Keep private or publish separate synthetic samples |
| Logs and runtime traces | Removed | Keep private |
| SQLite/DB ledgers | Removed | Keep private |
| Pickle/model artifacts | Removed | Keep private |
| Live execution modules | Removed | Public repo is architecture and decision contracts only |
| Proprietary strategy thresholds | Removed | Public repo shows governance, not edge |

## Public-Safe Content

- Architecture summary.
- Risk gate model.
- Decision-state contract.
- A deterministic, non-trading orchestrator example.
- Unit tests for the public orchestrator.
- Public-safe skill/orchestrator layer under `skills/`, limited to routing, evidence, safety, quality, and review contracts.

## Skill Layer Added

The second publication pass added `SKILL.md` files from the private workspace after excluding settings, caches, raw references, provider configs, credentials, live data, and runtime artifacts.

Included categories:

- Polymarket discovery, streaming, archive, microstructure, research, signal, risk, execution-compliance, and debugger skills.
- HB profitability and evidence-loop skills.
- Bot harness, status, memory, control-plane, and safety skills.
- Quality orchestration skills.

The skills may mention forbidden actions such as `.env`, private keys, VPS, PM2, or live orders only as safety boundaries. They do not contain actual credentials or live endpoint details.

## Gate Reminder

Create the GitHub repository as private first. Make it public only after a human review of this sanitized folder.
