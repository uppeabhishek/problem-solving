# Write your MySQL query statement below


SELECT customer_id, count(*) as count_no_trans from Visits where visit_id not in (select visit_id from transactions) group by customer_id;