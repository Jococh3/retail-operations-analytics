SELECT payment_type,COUNT(*) records,SUM(payment_value) total FROM order_payments GROUP BY payment_type;
