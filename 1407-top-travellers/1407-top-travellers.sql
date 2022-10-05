# Write your MySQL query statement below

select u.name, ifnull(sum(distance), 0) as travelled_distance from Users u LEFT JOIN Rides r on u.id = r.user_id group by u.id order by sum(r.distance) desc, u.name asc;