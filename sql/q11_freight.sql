SELECT state,SUM(freight)/NULLIF(SUM(revenue),0) freight_share FROM order_fact GROUP BY state ORDER BY freight_share DESC;
