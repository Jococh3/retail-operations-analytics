WITH s AS (SELECT DISTINCT seller_id,order_id,late FROM item_fact) SELECT seller_id,COUNT(late) eligible,AVG(late) late_rate FROM s GROUP BY seller_id HAVING COUNT(late)>=30 ORDER BY late_rate DESC;
