SELECT month,COUNT(*) orders,SUM(revenue) revenue,AVG(late) late_rate FROM order_fact GROUP BY month ORDER BY month;
