from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class MarketType(str, Enum):
    FIVE_MINUTE = "5m"
    FIFTEEN_MINUTE = "15m"


@dataclass(frozen=True)
class MarketTick:
    timestamp_ms: int
    asset: str
    condition_id: str
    outcome: str
    price: float
    best_bid: float
    best_ask: float
    seconds_left: int
    market_type: MarketType

    @property
    def spread(self) -> float:
        return round(self.best_ask - self.best_bid, 10)

    @property
    def executable_midpoint(self) -> float:
        return round((self.best_bid + self.best_ask) / 2, 10)


@dataclass(frozen=True)
class MicrostructureFeatures:
    book_imbalance_l1: float
    spot_delta_30s: float
    ofi_cumulative_epoch: float
    gap_since_last_tick_ms: int
    pre_open_price_delta: float | None = None


@dataclass(frozen=True)
class FillabilityCheck:
    implied_price: float
    best_ask: float
    max_acceptable_ask: float

    @property
    def can_attempt_limit_entry(self) -> bool:
        return self.best_ask <= self.max_acceptable_ask

    @property
    def implied_vs_executable_gap(self) -> float:
        return round(self.best_ask - self.implied_price, 10)

