# Private Exclusion Map

This repository was created from a much larger private workspace. The goal is to publish maximum reusable engineering value while excluding anything that could expose credentials, operational access, private data, or copy-paste trading edge.

## Excluded Categories

| Category | Why excluded |
|---|---|
| `.env` files | May contain API keys, private keys, wallet addresses, or runtime secrets. |
| SSH keys and PEM files | Direct infrastructure access risk. |
| VPS notes and process commands | Operational access and attack-surface risk. |
| Raw CSV/DB/parquet/pickle data | Large, private, and may include wallet, order, or runtime artifacts. |
| Runtime logs | May contain endpoints, tokens, paths, balances, or failure traces. |
| Live execution clients | Could be mistaken for production-ready trading code. |
| Exact strategy thresholds | Public repo should teach architecture, not leak the private edge. |
| Wallet studies | Potentially sensitive research and attribution risk. |

## Included Instead

- sanitized architecture maps
- public data contracts
- deterministic decision orchestrator
- risk and quality gates
- trade lifecycle scaffold
- synthetic fixtures
- skill/orchestrator layer after secret scanning
- continuation roadmap

## Re-publication Rule

Before adding anything from the private workspace:

```text
inspect -> classify -> sanitize -> test -> secret scan -> human review
```

If an artifact needs real credentials, real wallet data, raw logs, raw market dumps, or live endpoints to make sense, it should remain private.

