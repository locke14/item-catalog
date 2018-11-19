#!/usr/bin/python3

###############################################################################
# Database code for logs analytics
###############################################################################

import psycopg2
import datetime

###############################################################################

DBNAME = "news"

###############################################################################


def answer_q1():
    """What are the most popular three articles of all time?"""

    with psycopg2.connect(database=DBNAME) as db:
        with db.cursor() as c:
            c.execute('''
                        SELECT articles.title, COUNT(*) AS count
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
                print('"{:s}" - {:d} views'.format(result[0], result[1]))

            print()

###############################################################################


def answer_q2():
    """Who are the most popular article authors of all time?"""

    with psycopg2.connect(database=DBNAME) as db:
        with db.cursor() as c:
            c.execute('''
                        SELECT authors.name, COUNT(authors.name) AS count
                        FROM articles, authors, log
                        WHERE CONCAT('/article/', articles.slug) = log.path
                        AND authors.id = articles.author
                        GROUP BY authors.name
                        ORDER BY count desc;
            ''')

            print("-" * 80)
            print('2) Below are the most popular article authors of all time:')
            print("-" * 80)

            results = c.fetchall()
            for result in results:
                print('{:s} - {:d} views'.format(result[0], result[1]))

            print()

###############################################################################


def answer_q3():
    """On which days did more than 1% of requests lead to errors?"""

    with psycopg2.connect(database=DBNAME) as db:
        with db.cursor() as c:
            c.execute('''
                        SELECT errors.date, errors.count, total.count
                        FROM (
                                SELECT time::date AS date,
                                COUNT(time::date) AS count
                                FROM log
                                WHERE SUBSTRING(status, 1, 3)::integer >= 400
                                GROUP BY time::date
                            ) AS errors,
                            (
                                SELECT time::date AS date,
                                COUNT(time::date) AS count
                                FROM log
                                GROUP BY time::date
                            ) AS total
                        WHERE errors.date = total.date
                        AND errors.count > 0.01 * total.count;
            ''')

            print("-" * 80)
            print(r'3) Below are days where > 1% requests lead to errors:')
            print("-" * 80)

            results = c.fetchall()
            for result in results:
                date = result[0].strftime(r'%B %d, %Y')
                error_rate = 100 * result[1] / result[2]
                print(r'{:s} - {:.2f}% errors'.format(date, error_rate))

            print()

###############################################################################


if __name__ == '__main__':
    answer_q1()
    answer_q2()
    answer_q3()
