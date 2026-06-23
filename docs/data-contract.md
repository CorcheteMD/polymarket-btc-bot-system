# Public Data Contract

The private workspace used large tick, order-book, and replay files. Those files are intentionally excluded. This public contract describes the shape of data a continuation engineer would need.

## Market Tick

| Field | Type | Notes |
|---|---|---|
| `timestamp_ms` | integer | Local receive timestamp or normalized event timestamp |
| `asset` | string | Example: `BTC`, `ETH`, `SOL`; synthetic examples only |
| `condition_id` | string | Market identifier, not a private wallet or key |
| `outcome` | string | Binary side label |
| `price` | float | Last observed or implied price, not necessarily executable |
| `best_bid` | float | Best visible bid |
| `best_ask` | float | Best visible ask |
| `spread` | float | `best_ask - best_bid` |
| `seconds_left` | integer | Seconds until market resolution |
| `market_type` | string | Example: `5m`, `15m` |

## Microstructure Features

| Feature | Purpose |
|---|---|
| `book_imbalance_l1` | First-level order-book pressure |
| `spot_delta_30s` | External spot movement window |
| `ofi_cumulative_epoch` | Cumulative order-flow imbalance inside the epoch |
| `gap_since_last_tick_ms` | Detect stale or missing data |
| `pre_open_price_delta` | Compare pre-open and post-open behavior |

## Critical Distinction

An implied price is not the same as an executable ask. A continuation build must separate:

- observed/implied market price
- best bid
- best ask
- real fill evidence
- cash-truth reconciliation

Many trading systems fail by confusing "the price moved" with "I could have filled there."

