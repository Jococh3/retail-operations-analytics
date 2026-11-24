SELECT category,COUNT(*) items,SUM(price) revenue,SUM(freight_value) freight FROM item_fact GROUP BY category ORDER BY revenue DESC;
