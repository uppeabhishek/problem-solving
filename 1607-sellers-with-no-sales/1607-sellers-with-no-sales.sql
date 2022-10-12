# Write your MySQL query statement below

select s.seller_name from Seller s where s.seller_id not in (select o.seller_id from Orders o where year(o.sale_date) = 2020) order by s.seller_name;