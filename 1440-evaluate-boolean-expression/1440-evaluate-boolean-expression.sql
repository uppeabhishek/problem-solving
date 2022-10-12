# Write your MySQL query statement below

# select 
    # left_operand, operator, right_operand, (case 
    #     when operator = '=' then (case when l = r then 'true' else 'false' end) 
    #     when operator = '<' then (case when l < r then 'true' else 'false' end) 
    #     else (case when l > r then 'true' else 'false' end) 
    # end) as value
#         from (select *, (select value from Variables where name = left_operand) as l, (select value from Variables where name = right_operand) as r from Expressions) as t;

select 
    left_operand, operator, right_operand, (case 
        when operator = '=' then (case when v1.value = v2.value then 'true' else 'false' end) 
        when operator = '<' then (case when v1.value < v2.value then 'true' else 'false' end) 
        else (case when v1.value > v2.value then 'true' else 'false' end) 
    end) as value from Expressions e JOIN Variables v1 on e.left_operand = v1.name JOIN Variables v2 on e.right_operand = v2.name;