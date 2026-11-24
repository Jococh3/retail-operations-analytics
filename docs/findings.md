# Findings and quality review

## Reconciliation with Excel

The original cached KPI worksheet reports 99,441 orders, R$13,591,643.70 merchandise value, 96,470 eligible deliveries, 6,534 late and 89,936 on time. The new SQL and independent Python calculations agree on 99,441 orders and merchandise value. They include six additional orders with a delivery timestamp but a canceled status, yielding 96,476 eligible and 6,535 late. Eight additional orders marked delivered lack a delivery timestamp; these remain excluded. The 14 status/date inconsistencies are listed in `results/q12_discrepancies.csv`. Do not overwrite the source status without evidence. The original workbook is preserved; the new analysis uses timestamp eligibility consistently. Average elapsed delivery duration is 12.56 days in both approaches after rounding.

## Operational findings

- Alagoas (AL) has a 21.41% late rate among 397 eligible orders; Maranhão (MA) has 17.43% among 717. Investigate service coverage and seller mix before drawing conclusions.
- Mean review score is 4.29 for 89,448 on-time reviewed orders versus 2.27 for 6,382 late reviewed orders. A Mann–Whitney U test indicates a strong distributional difference (p below floating-point reporting precision; not literally zero). Confounding, selection bias and ties limit causal interpretation.
- Freight charges total R$2.25M. Compare state pairs and product mix before considering route or pricing changes.
- Seller risk reports require at least 30 eligible orders; use both rate and volume to prioritize investigation. Multi-seller orders cannot identify which seller caused a delay.

## Recommendations

Track eligible volume, late rate and average duration monthly; flag high-volume high-delay segments; investigate promised delivery dates, dispatch times and carrier performance with additional operational data. Review missing timestamps and status inconsistencies with source owners. Treat partial first and last months cautiously.

## Validation

Eight independent checks passed: unique order grain, order and item counts, merchandise and freight totals, eligibility, late count and duration. See validation.json. Excel cached values were inspected, not recalculated in Excel; native Power Query refresh was not tested.

An additional status-filtered check reproduced the Excel delivery metrics exactly: 96,470 eligible, 6,534 late, mean duration 12.558217 days. The item-bearing order average also matches Excel at R$137.754076. The original workbook was not modified.
