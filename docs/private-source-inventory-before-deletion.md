# Private Source Inventory Before Deletion

This is a sanitized inventory of the private workspace that produced this public repository.

It does not list credentials, hosts, wallet identifiers, private paths beyond category-level descriptions, or raw data contents.

## Approximate Shape

The private folder contained roughly:

| Category | Count observed |
|---|---:|
| CSV market/runtime data | 400+ |
| Python scripts/modules/tests | 360+ |
| Markdown docs/audits/research notes | 250+ |
| JSON configs/state/artifacts | 180+ |
| Shell/PowerShell scripts | 15+ |
| Images and misc artifacts | 10+ |

## Public Value Extracted

| Private area | Public artifact |
|---|---|
| Architecture maps | `docs/system-map.md`, `docs/architecture.md` |
| Data requirements | `docs/backtesting-data-requirements.md` |
| Execution feasibility | `docs/execution-feasibility-lessons.md` |
| Audit methodology | `docs/forensic-audit-playbook.md` |
| Bug prevention | `docs/bug-prevention-methodology.md` |
| Trade lifecycle design | `docs/trade-manager-design.md`, `src/trade_lifecycle.py` |
| Skill/orchestrator layer | `skills/` |
| Backtest safety method | `docs/backtest-methodology.md` |
| Sanitization boundary | `docs/private-exclusion-map.md`, `docs/sanitization-report.md` |

## Intentionally Not Extracted

- `.env` files
- private keys
- VPS/IP/process details
- Telegram tokens
- wallet studies
- raw CSVs and ledgers
- pickle/model artifacts
- exact private strategy parameters
- deploy scripts with operational assumptions
- raw logs

## If Rebuilding From This Repo

Start here:

1. `docs/backtesting-data-requirements.md`
2. `src/backtesting_schema.py`
3. `docs/backtest-methodology.md`
4. `docs/execution-feasibility-lessons.md`
5. `docs/trade-manager-design.md`
6. `docs/forensic-audit-playbook.md`

Then build adapters in a private repo for credentials, live endpoints, real data, and execution.

