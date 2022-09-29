# Write your MySQL query statement below

select DISTINCT t1.id,
case 
    when t1.p_id is null then 'Root'
    when t1.id = t2.p_id then 'Inner'
    else 'Leaf'
end as type
from Tree t1 LEFT JOIN Tree t2 ON t1.id = t2.p_id;