import psycopg2

DBNAME = 'news'

conn = psycopg2.connect(dbname=DBNAME)
cur = conn.cursor()
conn.execute("""select title, count(*) as num
             from articles left join log
             on lower(replace(title, '''', '')) like
             replace(replace(path, '/article/', ''), '-', ' ') || '%'
             group by title order by num desc""")

result = c.fetchall()[:3]
print(result)

db.close()
