import psycopg2

DBNAME = 'news'

def answer_questions(cur):

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

    cur.execute("""select *
                   from (
                   select total_access.day,
                   (error.count * 100) :: numeric / total_access.count as percentage
                   from total_access, error where total_access.day = error.day) a
                   where a.percentage > 1.0;""")

    error_rates = cur.fetchall()

    print('1. What are the most popular three articles of all time?')

    for item in articles_page_view:
        res_str = '{} ---- {} views'.format(item[0], item[1])
        print(res_str)
    print('\n')
    print('2. Who are the most popular article authors of all time? ')

    for item in authors_page_view:
        res_str = '{} ---- {} views'.format(item[0], item[1])
        print(res_str)
    print('\n')
    print('3. On which days did more than 1% of requests lead to errors?')

    for item in error_rates:
        res_str = '{} ---- {:.3}% errors'.format(item[0], item[1])
        print(res_str)
    print('\n')

if __name__ == '__main__':
    conn = psycopg2.connect(dbname=DBNAME)
    cursor = conn.cursor()
    answer_questions(cursor)
    conn.close()
