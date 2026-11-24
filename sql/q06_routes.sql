SELECT seller_state,state,COUNT(*) items,AVG(freight_value) mean_freight FROM item_fact GROUP BY seller_state,state HAVING COUNT(*)>=100 ORDER BY mean_freight DESC;
