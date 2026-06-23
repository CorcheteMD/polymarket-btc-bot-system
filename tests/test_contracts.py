import unittest

from src.contracts import FillabilityCheck, MarketTick, MarketType


class ContractsTest(unittest.TestCase):
    def test_spread_is_from_executable_book_not_implied_price(self) -> None:
        tick = MarketTick(
            timestamp_ms=1,
            asset="BTC",
            condition_id="synthetic-condition",
            outcome="UP",
            price=0.10,
            best_bid=0.09,
            best_ask=0.40,
            seconds_left=90,
            market_type=MarketType.FIVE_MINUTE,
        )
        self.assertEqual(tick.spread, 0.31)
        self.assertEqual(tick.executable_midpoint, 0.245)

    def test_fillability_blocks_when_ask_is_far_from_implied_price(self) -> None:
        check = FillabilityCheck(
            implied_price=0.05,
            best_ask=0.99,
            max_acceptable_ask=0.10,
        )
        self.assertFalse(check.can_attempt_limit_entry)
        self.assertEqual(check.implied_vs_executable_gap, 0.94)


if __name__ == "__main__":
    unittest.main()

