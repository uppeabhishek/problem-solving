# Write your MySQL query statement below

select 
    left_operand, operator, right_operand, (case 
        when operator = '=' then (case when l = r then 'true' else 'false' end) 
        when operator = '<' then (case when l < r then 'true' else 'false' end) 
        else (case when l > r then 'true' else 'false' end) 
    end) as value
        from (select *, (select value from Variables where name = left_operand) as l, (select value from Variables where name = right_operand) as r from Expressions) as t;