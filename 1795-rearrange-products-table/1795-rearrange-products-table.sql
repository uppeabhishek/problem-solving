# Write your MySQL query statement below


select product_id, 'store1' as store, (select store1 where product_id = product_id) as price from Products where store1 is not null union select product_id, 'store2' as store, (select store2 where product_id = product_id) as price from Products where store2 is not null union
select product_id, 'store3' as store, (select store3 where product_id = product_id) as price from Products where store3 is not null;