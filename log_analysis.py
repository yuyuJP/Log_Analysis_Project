import psycopg2

DBNAME = 'news'

conn = psycopg2.connect(dbname=DBNAME)
cur = conn.cursor()

# Execute three queries to solve questions.

# Fetch popular articles
cur.execute("""select title, count(*) as num from articles left join log
               on path like '%' || slug group by title order by num desc""")

# Use only top 3
articles_page_view = cur.fetchall()[:3]

# Fetch popular authors using view named id_page
cur.execute("""select name, num from authors, id_page
               where author = id order by num desc""")

authors_page_view = cur.fetchall()

print('1. What are the most popular three articles of all time?')

for item in articles_page_view:
    res_str = '{} ---- {} views'.format(item[0], item[1])
    print(res_str)

print('2. Who are the most popular article authors of all time? ')

for item in authors_page_view:
    res_str = '{} ---- {} views'.format(item[0], item[1])
    print(res_str)

conn.close()
