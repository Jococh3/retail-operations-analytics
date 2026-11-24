SELECT order_id,order_status,order_delivered_customer_date FROM order_fact WHERE (order_status='delivered')<>(order_delivered_customer_date IS NOT NULL);
