# Write your MySQL query statement below

# SELECT DISTINCT(s.sales_id) from 
#     Orders o 
#     JOIN SalesPerson s on s.sales_id = o.sales_id
#     where o.com_id = 1;
    
    
SELECT name from SalesPerson where sales_id not in (select sales_id from Orders where com_id = (select com_id from Company where name = 'RED'));