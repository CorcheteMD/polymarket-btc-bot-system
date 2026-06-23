import unittest

from src.backtesting_schema import (
    REQUIRED_PUBLIC_BACKTEST_FIELDS,
    compute_book_imbalance_l1,
    compute_btc_spot_delta_bps,
    validate_backtest_row,
)


class BacktestingSchemaTest(unittest.TestCase):
    def test_validate_backtest_row_fails_when_required_fields_are_missing(self) -> None:
        result = validate_backtest_row({"asset": "BTC"})

        self.assertFalse(result.valid)
        self.assertIn("best_ask", result.missing_fields)
        self.assertIn("recv_ts_ms", result.missing_fields)

    def test_validate_backtest_row_blocks_stale_books(self) -> None:
        row = {field: None for field in REQUIRED_PUBLIC_BACKTEST_FIELDS}
        row["book_stale_flag"] = True

        result = validate_backtest_row(row)

        self.assertFalse(result.valid)
        self.assertTrue(result.stale_book)
        self.assertEqual(result.missing_fields, ())

    def test_compute_book_imbalance_l1(self) -> None:
        result = compute_book_imbalance_l1(
            up_bid=100,
            up_ask=80,
            down_bid=60,
            down_ask=90,
        )

        self.assertAlmostEqual(result, 0.1515151515)

    def test_compute_btc_spot_delta_bps(self) -> None:
        result = compute_btc_spot_delta_bps(
            current_price=85000,
            prior_price=84900,
        )

        self.assertAlmostEqual(result, 11.7785630153)


if __name__ == "__main__":
    unittest.main()

