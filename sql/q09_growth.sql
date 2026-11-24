WITH m AS (SELECT month,SUM(revenue) revenue FROM order_fact GROUP BY month), p AS (SELECT *,LAG(revenue) OVER(ORDER BY month) prior FROM m) SELECT *, (revenue-prior)/NULLIF(prior,0) growth FROM p;
