SELECT state,COUNT(*) orders,COUNT(late) eligible,AVG(late) late_rate,AVG(delivery_days) mean_days FROM order_fact GROUP BY state ORDER BY late_rate DESC;
