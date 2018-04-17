import psycopg2

DBNAME = 'news'

conn = psycopg2.connect(dbname=DBNAME)
cur = conn.cursor()

# Fetch popular articles
cur.execute("""select title, count(*) as num from articles left join log
               on path like '%' || slug group by title order by num desc""")

# Use only top 3
result = cur.fetchall()[:3]

print('1. What are the most popular three articles of all time?')

for item in result:
    res_str = '{} ---- {} views'.format(item[0], item[1])
    print(res_str)

conn.close()
