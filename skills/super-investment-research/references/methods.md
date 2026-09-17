# Research methods

## Valuation

Use a model appropriate to the business and available information. Distinguish enterprise value from equity value and reconcile debt, cash, noncontrolling interests, and diluted shares where applicable. Do not mix currencies, fiscal periods, per-share figures, and totals.

Show the cash-flow or earnings basis, growth, margins, reinvestment, valuation assumptions, and sensitivity that materially affect the conclusion. Bear/base/bull cases are assumptions, not forecasts with established probabilities. Use arithmetic tools for calculations and show enough inputs for the result to be reproduced. If a critical input is absent, provide a conditional model rather than fabricated precision.

## Risk

Match returns to a stated frequency and price convention. Specify whether dividends, splits, fees, and currency conversion are included. Annualized volatility requires a stated sampling frequency and annualization assumption; do not compare daily and monthly estimates as if interchangeable.

Compute drawdown against the running high-water mark of the selected value series. Explain beta's benchmark and period. Historical VaR is an estimate conditional on the sample, not a maximum possible loss; define horizon, confidence level, method, and sign convention. Gap risk, illiquidity, and concentrated exposures can exceed historical estimates.

A simple stop-distance sizing example uses a stated loss budget divided by loss per unit including estimated friction. It is conditional on executable fills, not a guaranteed loss cap. Options require contract multipliers, scenario-dependent Greeks, spread liquidity, expiration, and assignment considerations; do not apply a stock sizing formula blindly.

## Backtests

Before running, define the universe, signal timing, entry, exit, sizing, rebalancing, and data availability rules. Eliminate discretionary rules that cannot be reproduced. Record data source/version and split dates.

Keep training, validation, and held-out evaluation separate. Signals must use information available at the decision time. Account for publication lags, delistings, survivorship, corporate actions, and execution timing. Avoid pretending a close-derived signal could trade at that same close without a valid execution model.

Model commissions, spread, slippage, liquidity, and any relevant borrowing or financing costs. Stress parameters, transaction friction, market regimes, and dependence on a few exceptional trades. Report trade count and uncertainty without asserting a universal minimum sample guarantees confidence.

Compare against a relevant benchmark and simple baseline. Report out-of-sample results separately from tuned results. If results are only user-supplied metrics, assess those metrics without claiming the underlying strategy was independently reproduced. Label all historical backtests SIMULATED; they do not establish future or live performance.
