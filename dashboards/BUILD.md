# Dashboard implementation guide

## Power BI Desktop — executive overview
Import `data/processed/order_fact.csv` as OrderFact. Set eligible and late to whole numbers (retain null late values), revenue/freight/delivery_days to decimal, month to text and date columns to datetime. Create these measures:

```dax
Orders = COUNTROWS(OrderFact)
Merchandise Value = SUM(OrderFact[revenue])
Freight Charges = SUM(OrderFact[freight])
Eligible Deliveries = SUM(OrderFact[eligible])
Late Deliveries = SUM(OrderFact[late])
Late Rate = DIVIDE([Late Deliveries], [Eligible Deliveries])
On Time Rate = IF([Eligible Deliveries] > 0, 1 - [Late Rate], BLANK())
Mean Delivery Days = CALCULATE(AVERAGE(OrderFact[delivery_days]), OrderFact[eligible] = 1)
```
Use cards for orders, merchandise, late rate and mean days. Add a monthly revenue line, state late-rate bar chart (filter eligible count >=100), and month/state slicers. Format currency BRL and rates as percentages. Save as Retail_Operations.pbix. With no filters, verify 99,441 orders, 96,476 eligible, 6,535 late and R$13,591,643.70 merchandise.

## Tableau Desktop — diagnostic view
Connect separately to `results/q04_seller.csv`, `q06_routes.csv`, `q03_state.csv` and `q07_reviews.csv`. Build seller risk bars (late_rate, eligible in tooltip), state risk bars, seller-state/customer-state freight heatmap (mean_freight, items in tooltip), and review comparison. Format rates as percentages. Do not sum rates or join these aggregated tables. Assemble a dashboard with independent sheet filters; save as packaged workbook TWBX. Validate against the corresponding CSVs. Native files are not included or tested.
