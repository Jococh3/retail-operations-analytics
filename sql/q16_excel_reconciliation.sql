SELECT COUNT(*) eligible,SUM(late) late,AVG(delivery_days) mean_days FROM order_fact WHERE eligible=1 AND order_status='delivered';
