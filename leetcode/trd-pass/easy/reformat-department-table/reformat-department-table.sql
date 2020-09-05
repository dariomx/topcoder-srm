with
  dept as (select distinct id from department),
  jan as (select id,revenue from department where month='Jan'),
  feb as (select id,revenue from department where month='Feb'),
  mar as (select id,revenue from department where month='Mar'),
  apr as (select id,revenue from department where month='Apr'),
  may as (select id,revenue from department where month='May'),
  jun as (select id,revenue from department where month='Jun'),
  jul as (select id,revenue from department where month='Jul'),
  aug as (select id,revenue from department where month='Aug'),
  sep as (select id,revenue from department where month='Sep'),
  oct as (select id,revenue from department where month='Oct'),
  nov as (select id,revenue from department where month='Nov'),
  dic as (select id,revenue from department where month='Dec')
select
  id,
  jan.revenue as "Jan_Revenue",
  feb.revenue as "Feb_Revenue",
  mar.revenue as "Mar_Revenue",
  apr.revenue as "Apr_Revenue",
  may.revenue as "May_Revenue",
  jun.revenue as "Jun_Revenue",
  jul.revenue as "Jul_Revenue",
  aug.revenue as "Aug_Revenue",
  sep.revenue as "Sep_Revenue",
  oct.revenue as "Oct_Revenue",
  nov.revenue as "Nov_Revenue",
  dic.revenue as "Dec_Revenue"
from
  dept left join
  jan using(id) left join
  feb using(id) left join
  mar using(id) left join
  apr using(id) left join
  may using(id) left join
  jun using(id) left join
  jul using(id) left join
  aug using(id) left join
  sep using(id) left join
  oct using(id) left join
  nov using(id) left join
  dic using(id)
order by id;
