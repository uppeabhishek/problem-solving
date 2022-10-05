# Write your MySQL query statement below


select Email from Person p group by email having count(email) > 1;