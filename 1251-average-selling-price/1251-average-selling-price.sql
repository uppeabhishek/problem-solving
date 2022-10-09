# Write your MySQL query statement below

select u.product_id, round(sum(u.units * p.price) / sum(u.units), 2) as average_price from Prices p RIGHT JOIN UnitsSold u on u.product_id = p.product_id and u.purchase_date >= p.start_date and u.purchase_date <= p.end_date group by u.product_id;