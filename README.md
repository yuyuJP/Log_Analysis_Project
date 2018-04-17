# Log_Analysis_Project
This repository is for Udacity Full Stack Web Developer Nanodegree Program Submission

# Create View
First, you have to create three views named `id_page`, `total_access` and `error` to run `log_analysis.py`.
You can create the three views by executing these sql queries:
```
 create view id_page as select author, count(*) as
 num from articles left join log
 on path like '%' || slug
 group by author order by num desc;
```

```
create view total_access as select day :: date,
count(*) from log, date_trunc('day', time) as day
group by day order by day;
```

```
create view error as select day :: date, count(*)
from log, date_trunc('day', time) as day
where status = '404 NOT FOUND'
group by day order by day;
```
