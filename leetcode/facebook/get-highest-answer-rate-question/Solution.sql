select question_id as survey_log
from
(
  select
    question_id,
    count(*) cnt
  from survey_log
  where action = 'answer'
  group by question_id
  order by cnt desc
) tmp
limit 1;


