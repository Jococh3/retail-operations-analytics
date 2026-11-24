SELECT CASE late WHEN 1 THEN 'Late' ELSE 'On time' END delivery_group,COUNT(*) orders,AVG(review_score) mean_review FROM order_fact WHERE late IS NOT NULL AND review_score IS NOT NULL GROUP BY late;
