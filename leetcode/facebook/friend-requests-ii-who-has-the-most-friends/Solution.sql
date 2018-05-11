select *
from
(
  select id, count(*) num
  from
  (
    select accepter_id id, requester_id as fid
    from request_accepted
    union all
    select requester_id id, accepter_id as fid
    from request_accepted
  ) acc_req
  group by id
  order by num desc
) id_num
limit 1;


