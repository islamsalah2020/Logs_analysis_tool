#!/usr/bin/python

import psycopg2


# connecting to Database news to can retrieve data
def connect(db_name="news"):
    try:
        db = psycopg2.connect(dbname=db_name)
        return db
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# List the top 3 favorite articles.
def top_articles():
    db = connect()
    cur = db.cursor()
    query1 = """SELECT title, count(*) as num
            FROM log , articles
            WHERE status='200 OK' and replace(path, '/article/', '') = slug
            GROUP BY title
            order by num desc
            LIMIT 3"""
    cur.execute(query1)
    res = cur.fetchall()
    print('\nthe most popular three articles of all time:')
    j = 1
    for i in res:
        print '{} {}, {} views'.format(j, i[0], i[1])  # title, no. of views
        j = j + 1
    cur.close()
    db.close()


# List the top 3 popular authors.
def top_authors():
    db = connect()
    cur = db.cursor()
    query2 = """SELECT name, (articles_view.num) as num FROM  authors,
    articles_view WHERE authors.id = articles_view.author
    GROUP BY name, num order by num desc LIMIT 3"""
    cur.execute(query2)
    res = cur.fetchall()
    print('\nthe most popular article authors of all time:')
    j = 1
    for i in res:
        print '{} {}, {} views'.format(j, i[0], i[1])
        j = j + 1
    cur.close()
    db.close()


def error_percentage():
    db = connect()
    cur = db.cursor()
    query3 = """select * from error_rate where ratio > 1"""
    cur.execute(query3)
    res = cur.fetchall()
    print('\nThe days with error rate more than 1% :')
    for i in res:
        print('{}, {}% errors'.format(i[0], i[1]))
    cur.close()
    db.close()


if __name__ == '__main__':
    top_articles()
    top_authors()
    error_percentage()
