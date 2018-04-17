# Log_Analysis_Project
This repository is for Udacity Full Stack Web Developer Nanodegree Program Submission

# Create View
First, you have to create view named `id_page` to run `log_analysis.py` following this command
```
 create view id_page as select author, count(*) as
 num from articles left join log
 on path like '%' || slug
 group by author order by num desc; 
```
