# Local calculations

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

Use `python "<skill-dir>/scripts/calculate.py" MODE input.json`. These helpers fetch no data and issue no orders. Supply reconciled units, dates and assumptions; results describe the inputs, not current market conditions.

| MODE | Input | Meaning |
|---|---|---|
| valuation | `{"profit":100,"pe":12,"net_debt":0,"shares":50}` | Equity earnings times PE, then divided by matching diluted shares. Profit and shares must use compatible scale. PE already values equity; nonzero net_debt is rejected to prevent subtracting debt twice. |
| terminal-pe | `{"growth":0.03,"discount_rate":0.10,"roic":0.15}` | Steady-state reinvestment model (1-g/ROIC)/(r-g). Requires r>g, ROIC>0 and g<ROIC. A policy assumption is not a measured terminal multiple. |
| position | `{"equity":10000,"risk_fraction":0.01,"entry":50,"stop":48}` | Long-only whole-share size, capped by both risk budget and available equity. No leverage, fees or gap/slippage model. |
| xirr | `{"cashflows":[{"date":"2025-01-01","amount":-100},{"date":"2026-01-01","amount":110}]}` | ACT/365 cash-flow IRR. Supports one initial negative cash flow and later nonnegative receipts. Multiple sign changes are rejected because roots can be ambiguous. |

Exit 2 means invalid inputs or unsupported numerical conditions. Distinguish a dated-cash-flow IRR from terminal-price CAGR plus a payout approximation. Do not relabel earnings times PE as enterprise value. The terminal model is simplified and its growth/ROIC assumptions require research.

Keep a dated thesis snapshot: evidence, valuation assumptions, uncertainty, catalysts, falsification conditions and the next check. Compare new evidence with that snapshot rather than repeating a stale report. Select market-regime, company-quality, setup, portfolio-risk or historical-backtest methods to match the question. External provider contracts, strategy engines and broker execution remain separate integrations; do not claim them installed.

The XIRR solver uses a finite bracket from -0.999999999 through an expanding upper bound of at most 1073741823. A root beyond it fails explicitly; it is not approximated as the boundary.
