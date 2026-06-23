from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping


IDENTITY_FIELDS = frozenset(
    {
        "timestamp",
        "asset",
        "market",
        "condition_id",
        "outcome",
        "token_dir",
    }
)

PRICE_BOOK_FIELDS = frozenset(
    {
        "price",
        "best_bid",
        "best_ask",
        "spread",
        "up_bid",
        "up_ask",
        "down_bid",
        "down_ask",
        "book_imbalance_l1",
    }
)

TIMING_FIELDS = frozenset(
    {
        "secs_left",
        "secs_to_open",
        "event_type",
        "tick_sequence_epoch",
        "gap_since_last_tick",
        "ms_since_epoch_open",
        "epoch_duration_s",
    }
)

PROVENANCE_FIELDS = frozenset(
    {
        "source_ts_ms",
        "recv_ts_ms",
        "latency_ms",
        "event_source",
        "event_type_raw",
        "is_synthetic_tick",
        "ws_session_id",
        "reconnect_seq",
        "up_book_ts_ms",
        "down_book_ts_ms",
        "cross_book_skew_ms",
        "book_stale_flag",
        "tick_size",
        "is_trade_event",
        "is_book_event",
        "is_price_change_event",
        "ingest_seq",
        "warmup_flag",
    }
)

REQUIRED_PUBLIC_BACKTEST_FIELDS = (
    IDENTITY_FIELDS | PRICE_BOOK_FIELDS | TIMING_FIELDS | PROVENANCE_FIELDS
)


@dataclass(frozen=True)
class SchemaValidationResult:
    valid: bool
    missing_fields: tuple[str, ...]
    stale_book: bool


def validate_backtest_row(
    row: Mapping[str, object],
    *,
    required_fields: Iterable[str] = REQUIRED_PUBLIC_BACKTEST_FIELDS,
) -> SchemaValidationResult:
    missing = tuple(sorted(field for field in required_fields if field not in row))
    return SchemaValidationResult(
        valid=not missing and not bool(row.get("book_stale_flag", False)),
        missing_fields=missing,
        stale_book=bool(row.get("book_stale_flag", False)),
    )


def compute_book_imbalance_l1(
    *,
    up_bid: float,
    up_ask: float,
    down_bid: float,
    down_ask: float,
) -> float:
    denominator = up_bid + up_ask + down_bid + down_ask
    if denominator <= 0:
        raise ValueError("book sizes must produce a positive denominator")
    value = (up_bid + down_ask - up_ask - down_bid) / denominator
    return round(value, 10)


def compute_btc_spot_delta_bps(*, current_price: float, prior_price: float) -> float:
    if prior_price <= 0:
        raise ValueError("prior_price must be positive")
    return round(((current_price - prior_price) / prior_price) * 10000, 10)

