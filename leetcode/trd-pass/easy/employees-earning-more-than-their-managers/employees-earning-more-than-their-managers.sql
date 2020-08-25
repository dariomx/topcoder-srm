/* Write your PL/SQL query statement below */
select e.name as employee
from employee e join
     employee m ON (e.managerId = m.id AND e.salary > m.salary);

