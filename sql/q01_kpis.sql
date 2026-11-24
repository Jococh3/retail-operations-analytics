SELECT COUNT(*) orders,SUM(revenue) revenue,SUM(freight) freight,SUM(eligible) eligible,SUM(late) late,AVG(late) late_rate,AVG(delivery_days) mean_days FROM order_fact;
