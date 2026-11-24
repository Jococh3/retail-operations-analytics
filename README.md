# Retail Operations Analytics | Olist

This portfolio project examines order fulfillment, freight costs, merchandise revenue and customer satisfaction using the [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). The goal is to identify operational questions worth investigating, not to claim that a real business adopted the recommendations.

## Run the analysis

From the project root, install dependencies with `python -m pip install -r requirements.txt`, then run `python python/run_analysis.py`. This rebuilds the SQLite database, executes 15 SQL reports, exports dashboard-ready tables and checks key totals independently against the raw CSVs. Python 3.10+ is recommended. The database is rebuilt on every run.

## Contents

- `excel/`: original Excel workbook, preserved unchanged.
- `data/raw/`: nine original source CSVs; consult the dataset page for redistribution terms before publishing.
- `data/processed/`: generated order and item facts and SQLite database.
- `sql/`: views and 15 executable analytical queries.
- `python/`: reproducible processing, validation and statistical analysis.
- `results/`: query outputs, charts and validation evidence.
- `dashboards/`: native dashboard build instructions; no verified PBIX or TWB is supplied.
- `docs/`: findings, reconciliation and interview preparation.

## Main findings

The data contains 99,441 orders and 112,650 order items, with R$13.59 million in recorded merchandise value and R$2.25 million in freight charges. Using delivery timestamps regardless of status, 6,535 of 96,476 eligible orders were late (6.77%). Orders with reviews averaged 4.29 stars when on time versus 2.27 when late. These are historical associations, not causal estimates.

## Methodology

The order fact has one row per order; item totals and review scores are aggregated before joining to avoid multiplying revenue. Late means the actual delivery calendar date is after the estimated calendar date. Missing dates are excluded from the rate. Merchandise value includes recorded items regardless of order status; it is not recognized accounting revenue. Review scores are averaged within orders when multiple reviews exist. Seller reports count distinct seller/order pairs, so totals across sellers are not additive. Route reports use seller and customer states, not actual carrier routes. Freight is the recorded charge, not necessarily carrier cost. The original workbook uses a narrower delivery eligibility rule; see `docs/findings.md`.

## Status

SQL and Python reports have been executed and validated. Native Power BI and Tableau dashboards still need to be assembled and checked in their respective desktop applications. This expanded version was developed with AI assistance; review and rerun it before representing the new work as your own experience.
