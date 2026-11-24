WITH s AS (SELECT state,COUNT(late) eligible,AVG(late) late_rate FROM order_fact GROUP BY state HAVING COUNT(late)>=100) SELECT *,DENSE_RANK() OVER(ORDER BY late_rate DESC) risk_rank FROM s;
