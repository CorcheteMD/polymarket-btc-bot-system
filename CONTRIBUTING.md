# Contributing

This repository is a sanitized case study. Contributions should improve architecture, testing, documentation, or safety controls.

## Allowed Contributions

- Add or improve deterministic decision contracts.
- Add unit tests for risk-gate behavior.
- Improve docs, diagrams, and continuation guides.
- Add synthetic examples that do not encode private strategy parameters.
- Add adapters as interfaces or mocks, not live trading clients.

## Not Allowed

- Credentials, private keys, wallet addresses, VPS IPs, Telegram tokens, or environment dumps.
- Raw market datasets, logs, SQLite ledgers, model artifacts, or private backtest exports.
- Live execution code that can place or cancel orders.
- Proprietary thresholds, wallet seeds, or copy-paste strategy edge.

## Development

```bash
python -m unittest discover -s tests
```

## Safety Review

Before opening a pull request, check:

- No secret-like strings.
- No `.env`, `*.pem`, `*.csv`, `*.db`, `*.pkl`, or logs.
- No live endpoint or infrastructure detail.
- Tests still pass.

