from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum


class TradeState(str, Enum):
    PENDING = "pending"
    OPEN = "open"
    CLOSING = "closing"
    CLOSED = "closed"
    RECOVERED_OPEN = "recovered_open"


@dataclass(frozen=True)
class TradeRecord:
    trade_id: str
    condition_id: str
    outcome: str
    state: TradeState
    entry_price: float
    size: float
    opened_at_ms: int
    closed_at_ms: int | None = None
    exit_price: float | None = None
    net_pnl: float | None = None

    @property
    def is_terminal(self) -> bool:
        return self.state == TradeState.CLOSED

    @property
    def exposure(self) -> float:
        if self.is_terminal:
            return 0.0
        return round(self.entry_price * self.size, 10)


class TradeLifecycle:
    def __init__(self) -> None:
        self._records: dict[str, TradeRecord] = {}

    def open_trade(
        self,
        *,
        trade_id: str,
        condition_id: str,
        outcome: str,
        entry_price: float,
        size: float,
        opened_at_ms: int,
    ) -> TradeRecord:
        if trade_id in self._records:
            raise ValueError(f"trade already exists: {trade_id}")
        if entry_price <= 0 or size <= 0:
            raise ValueError("entry_price and size must be positive")

        record = TradeRecord(
            trade_id=trade_id,
            condition_id=condition_id,
            outcome=outcome,
            state=TradeState.OPEN,
            entry_price=entry_price,
            size=size,
            opened_at_ms=opened_at_ms,
        )
        self._records[trade_id] = record
        return record

    def close_trade(
        self,
        *,
        trade_id: str,
        exit_price: float,
        closed_at_ms: int,
        fee_rate: float = 0.0,
    ) -> TradeRecord:
        record = self._records[trade_id]
        if record.is_terminal:
            return record
        if exit_price < 0:
            raise ValueError("exit_price must be non-negative")
        if fee_rate < 0:
            raise ValueError("fee_rate must be non-negative")

        gross = (exit_price - record.entry_price) * record.size
        fees = (exit_price * record.size) * fee_rate
        closed = replace(
            record,
            state=TradeState.CLOSED,
            closed_at_ms=closed_at_ms,
            exit_price=exit_price,
            net_pnl=round(gross - fees, 10),
        )
        self._records[trade_id] = closed
        return closed

    def recover_open_trades(self) -> list[TradeRecord]:
        recovered: list[TradeRecord] = []
        for trade_id, record in list(self._records.items()):
            if not record.is_terminal:
                updated = replace(record, state=TradeState.RECOVERED_OPEN)
                self._records[trade_id] = updated
                recovered.append(updated)
        return recovered

    def total_exposure(self) -> float:
        return round(sum(record.exposure for record in self._records.values()), 10)

    def get(self, trade_id: str) -> TradeRecord:
        return self._records[trade_id]

