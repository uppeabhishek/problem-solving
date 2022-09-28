# Write your MySQL query statement below

select * from Patients where conditions like '% DIAB1%' or SUBSTRING_INDEX(conditions, " ", 1) like "DIAB1%"