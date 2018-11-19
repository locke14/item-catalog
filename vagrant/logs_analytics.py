#!/usr/bin/python3

###############################################################################
# Database code for logs analytics
###############################################################################

import psycopg2

###############################################################################

DBNAME = "news"

###############################################################################

def answer_q1():
    """What are the most popular three articles of all time?"""

    with psycopg2.connect(database=DBNAME) as db:
        with db.cursor() as c:
            c.execute('''
                        SELECT articles.title, count(*) as count
                        FROM articles, log
                        WHERE CONCAT('/article/', articles.slug) = log.path
                        GROUP BY articles.title
                        ORDER BY count desc;
            ''')

            print("-" * 80)
            print('1) Below are the three most popular articles of all time:')
            print("-" * 80)

            results = c.fetchmany(3)
            for result in results:
                print('"{}" - {} views'.format(result[0], result[1]))

            print()

###############################################################################

def answer_q2():
    """Who are the most popular article authors of all time?"""
    pass

###############################################################################

def answer_q3():
    """On which days did more than 1% of requests lead to errors?"""
    pass

###############################################################################

if __name__ == '__main__':
    answer_q1()
    answer_q2()
    answer_q3()
