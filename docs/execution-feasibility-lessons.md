# Execution Feasibility Lessons

The highest-value lesson from the private research was not a parameter. It was a correction to the mental model.

## Implied Price Is Not Executable Price

Prediction-market data often exposes an implied or last-trade price. That number can make a token look cheap. It does not prove there is a seller at that price.

For execution logic, the bot must reason from the order book:

- `implied_price`: useful for research and market state.
- `best_bid`: what buyers are currently willing to pay.
- `best_ask`: what sellers are currently asking.
- `spread`: the executable gap between those two prices.
- `fillability`: whether a proposed entry can plausibly be filled without crossing into a bad price.

The public rule is:

```text
No fillability, no trade.
```

## Common Failure Pattern

```text
candidate looks cheap by implied price
  -> bot assumes it can buy near implied price
  -> actual best ask is far away
  -> live execution crosses a bad spread
  -> backtest edge disappears
```

This is why the repository includes `FillabilityCheck` and public tests around the implied-vs-executable gap.

## Safer Architecture

```text
observe implied dislocation
  -> inspect executable order book
  -> reject wide gaps
  -> post bounded limit intent
  -> wait for fill or cancel
  -> only manage exits after a real fill
```

Market orders and loosely bounded buys are excluded from this public scaffold.

## What To Validate Before Promotion

- Does the dataset distinguish implied price, last trade, bid, and ask?
- Does the backtest assume fills at prices that were not available?
- Are fees, spread, slippage, and partial fills modeled?
- Does every promoted candidate have cash truth, not just simulated PnL?
- Can the system cancel stale limit intent when the market regime changes?

