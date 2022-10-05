# Write your MySQL query statement below

# select product_id, product_name from (select p.product_id, (case when sum(case when s.sale_date >= '2019/01/01' and s.sale_date <= '2019/03/31' then 1 else 0 end) = count(s.product_id) then p.product_name end) as product_name from Product p JOIN Sales s on p.product_id = s.product_id group by s.product_id) as t1 where product_name is not null;


select p.product_id, p.product_name from Product p JOIN Sales s on p.product_id = s.product_id group by s.product_id having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31';