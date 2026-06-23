# Backtesting Data Requirements

This document describes what a builder should collect before trusting a Polymarket BTC backtest.

The core lesson is simple:

```text
capture maximum context now; missing market data cannot be recovered later
```

This is a public-safe collector contract. It excludes private strategy thresholds, wallet studies, live endpoints, and operational deployment details.

## Minimum Useful Dataset

A toy backtest can run on timestamp, price, and outcome. A serious execution-aware backtest cannot.

The minimum useful dataset must separate:

- implied or last-trade price
- executable bid/ask
- timing inside the market epoch
- BTC spot context
- order-book freshness
- event provenance
- final resolution label

## Recommended Schema

The private collector design converged on two layers:

- **Base research schema:** 46 logical fields.
- **Operational hardening schema:** 21 additional provenance/freshness fields.

Together, the recommended collector emits **67 fields**.

## Field Groups

### 1. Identity

| Field | Purpose |
|---|---|
| `timestamp` | Human-readable event timestamp. |
| `asset` | Asset family, for example `BTC`. |
| `market` | Public market slug or normalized market label. |
| `condition_id` | Prediction-market condition identifier. |
| `outcome` | Binary side, for example `UP` or `DOWN`. |
| `token_dir` | Directional token label used internally by the collector. |

### 2. Price And L1 Book

| Field | Purpose |
|---|---|
| `price` | Last observed or implied price. Not necessarily executable. |
| `best_bid` | Best visible bid for this outcome. |
| `best_ask` | Best visible ask for this outcome. |
| `spread` | `best_ask - best_bid`. |
| `up_bid` / `up_ask` | L1 book for the Up side. |
| `down_bid` / `down_ask` | L1 book for the Down side. |
| `book_imbalance_l1` | Cross-side L1 pressure feature. |

### 3. Depth And Extremes

| Field | Purpose |
|---|---|
| `book_min_price` | Lowest visible book price captured by the parser. |
| `book_max_price` | Highest visible book price captured by the parser. |

L2-L5 depth is useful if the API/feed supports it, but L1 plus min/max is a strong first public contract.

### 4. Flow And Microstructure

| Field | Purpose |
|---|---|
| `ofi_delta` | Outcome-side order-flow imbalance for the current tick. |
| `ofi_cumul_epoch` | Cumulative OFI from the start of the market epoch. |
| `maker_taker_ratio` | Experimental maker/taker proxy from raw trade fields. |
| `size` | Trade or book-update size, depending on event type. |

`maker_taker_ratio` should be captured but quarantined until validated against real payload semantics.

### 5. Timing And Sequence

| Field | Purpose |
|---|---|
| `secs_left` | Seconds until market close/resolution. |
| `secs_to_open` | Seconds until market opens; negative during pre-open capture. |
| `event_type` | Normalized event type. |
| `tick_sequence_epoch` | Monotonic tick counter inside the epoch. |
| `gap_since_last_tick` | Milliseconds since previous collected tick. |
| `ms_since_epoch_open` | Milliseconds from epoch open. |
| `epoch_duration_s` | Expected epoch length, such as 300 or 900 seconds. |

### 6. Epoch Context

| Field | Purpose |
|---|---|
| `market_type` | Public timeframe label, such as `5m` or `15m`. |
| `phase` | Normalized phase, for example pre-open/open/closing. |
| `epoch_open_ts` | Absolute epoch open timestamp. |
| `epoch_number_day` | Epoch count within UTC day. |
| `hour_utc` | UTC hour extracted from receive timestamp. |
| `day_of_week` | UTC day-of-week feature. |

### 7. BTC Spot Context

| Field | Purpose |
|---|---|
| `btc_price` | BTC spot price aligned to the market event. |
| `btc_open` | BTC price at epoch open. |
| `btc_spot_delta_1s` | BTC move over 1 second, in basis points. |
| `btc_spot_delta_30s` | BTC move over 30 seconds, in basis points. |
| `btc_spot_delta_300s` | BTC move over 300 seconds, in basis points. |

Spot deltas should use a wall-clock ring buffer, not “last N rows.” Rows are not seconds.

### 8. Cross-Epoch State

| Field | Purpose |
|---|---|
| `prev_winner` | Previous epoch resolved winner. |
| `prev_open_price` | Previous epoch opening price. |
| `pre_open_price_delta` | Price movement from last pre-open tick to first post-open tick. |

### 9. Metadata And Accumulators

| Field | Purpose |
|---|---|
| `strike_price` | Market strike/reference price if available. |
| `sum_min` | Public aggregate/minimum field if used by the collector. |
| `volume_epoch_cumul` | Cumulative volume inside epoch. |
| `trade_count_epoch` | Cumulative trade count inside epoch. |

## Provenance And Freshness Fields

These fields are what make the dataset trustworthy enough for ML or execution-aware research.

### Raw Identity And Market Clock

| Field | Purpose |
|---|---|
| `market_id` | Raw public market identifier from the data source. |
| `clob_asset_id` | Raw CLOB asset/token identifier. |
| `epoch_close_ts` | Absolute close timestamp used to compute epoch timing. |

### Source And Receive Clock

| Field | Purpose |
|---|---|
| `source_ts_ms` | Timestamp from the source payload. |
| `recv_ts_ms` | Local receive timestamp. |
| `latency_ms` | `recv_ts_ms - source_ts_ms`. |
| `event_source` | `ws`, `poll`, `heartbeat`, or `derived`. |
| `event_type_raw` | Original event type from the payload. |
| `is_synthetic_tick` | True when the row is generated rather than directly observed. |
| `ws_session_id` | Connection/session identifier. |
| `reconnect_seq` | Reconnect counter for the collector process. |

### Cross-Side Freshness

| Field | Purpose |
|---|---|
| `up_book_ts_ms` | Last valid source timestamp for Up book. |
| `down_book_ts_ms` | Last valid source timestamp for Down book. |
| `cross_book_skew_ms` | Absolute timestamp skew between Up and Down book snapshots. |
| `book_stale_flag` | True when the book is too old or cross-side data is misaligned. |

### Event Lineage And Quality

| Field | Purpose |
|---|---|
| `tick_size` | Active tick size for the market event. |
| `is_trade_event` | True for real trade events. |
| `is_book_event` | True for book updates. |
| `is_price_change_event` | True for price-change events. |
| `ingest_seq` | Local monotonic sequence number. |
| `warmup_flag` | True while rolling windows do not have enough history. |

## Hard Rules

- Do not compute cross-side features when `book_stale_flag == true`.
- Mark `book_stale_flag == true` when cross-side book skew is too large.
- Mark `book_stale_flag == true` when either side of the book is stale relative to `recv_ts_ms`.
- `epoch_open_ts = epoch_close_ts - epoch_duration_s`.
- `tick_sequence_epoch` starts at `0` and resets when the epoch changes.
- `gap_since_last_tick` is `0` only for the first tick in an epoch.
- Backtests must model fills from `best_bid` and `best_ask`, not from implied `price`.
- Resolution labels should come from the fastest reliable source and be reconciled later if needed.

## Feature Formulas

### Cross-Side L1 Book Imbalance

```text
book_imbalance_l1 =
  (up_bid + down_ask - up_ask - down_bid)
  / (up_bid + up_ask + down_bid + down_ask)
```

Expected range: `[-1, 1]`.

### Outcome-Side OFI

```text
ofi_delta = delta_bid_size - delta_ask_size
```

Positive OFI means bid pressure increased or ask pressure decreased.

### Cumulative OFI

```text
if tick_sequence_epoch == 0:
  ofi_cumul_epoch = ofi_delta
else:
  ofi_cumul_epoch = previous_ofi_cumul_epoch + ofi_delta
```

### BTC Spot Delta

```text
btc_spot_delta_Xs =
  (btc_price_now - btc_price_at_or_before_now_minus_Xs)
  / btc_price_at_or_before_now_minus_Xs
  * 10000
```

Use the latest real tick at or before the target timestamp. Do not invent interpolated prices for this contract.

### Pre-Open Price Delta

```text
pre_open_price_delta =
  first_post_open_price - last_pre_open_price
```

## Implementation Priority

1. Capture identity, timing, L1 book, raw source timestamps, and `condition_id`.
2. Add epoch sequence fields: `tick_sequence_epoch`, `gap_since_last_tick`, `ms_since_epoch_open`.
3. Add BTC spot ring-buffer deltas.
4. Add OFI and cumulative OFI.
5. Add cross-epoch fields: `prev_winner`, `prev_open_price`, `pre_open_price_delta`.
6. Add depth/extreme fields if available.
7. Capture maker/taker raw fields, but keep derived ratios experimental until validated.

## What Not To Publish

- private keys or `.env` files
- VPS/IP/process notes
- raw wallet studies
- full raw ledgers
- private strategy thresholds
- operational command history
- unreviewed logs

