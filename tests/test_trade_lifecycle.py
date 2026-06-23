import unittest

from src.trade_lifecycle import TradeLifecycle, TradeState


class TradeLifecycleTest(unittest.TestCase):
    def test_close_trade_is_idempotent(self) -> None:
        lifecycle = TradeLifecycle()
        lifecycle.open_trade(
            trade_id="t1",
            condition_id="synthetic-condition",
            outcome="DOWN",
            entry_price=0.10,
            size=100,
            opened_at_ms=1,
        )

        first = lifecycle.close_trade(
            trade_id="t1",
            exit_price=0.14,
            closed_at_ms=2,
            fee_rate=0.02,
        )
        second = lifecycle.close_trade(
            trade_id="t1",
            exit_price=0.01,
            closed_at_ms=3,
            fee_rate=0.02,
        )

        self.assertEqual(first, second)
        self.assertEqual(second.state, TradeState.CLOSED)
        self.assertEqual(second.net_pnl, 3.72)
        self.assertEqual(lifecycle.total_exposure(), 0.0)

    def test_recovery_marks_non_terminal_trades(self) -> None:
        lifecycle = TradeLifecycle()
        lifecycle.open_trade(
            trade_id="t1",
            condition_id="synthetic-condition",
            outcome="UP",
            entry_price=0.20,
            size=50,
            opened_at_ms=1,
        )

        recovered = lifecycle.recover_open_trades()

        self.assertEqual(len(recovered), 1)
        self.assertEqual(recovered[0].state, TradeState.RECOVERED_OPEN)
        self.assertEqual(lifecycle.total_exposure(), 10.0)

    def test_invalid_open_inputs_are_rejected(self) -> None:
        lifecycle = TradeLifecycle()

        with self.assertRaises(ValueError):
            lifecycle.open_trade(
                trade_id="bad",
                condition_id="synthetic-condition",
                outcome="UP",
                entry_price=0,
                size=10,
                opened_at_ms=1,
            )


if __name__ == "__main__":
    unittest.main()

