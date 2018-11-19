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

    print('Q1---------------------------------------------------------------')
    print('Below are the three most popular articles of all time:')
    print('1. ')
    print('2. ')
    print('3. ')
    print()

###############################################################################

def answer_q2():
    """Who are the most popular article authors of all time?"""

    print('Q2---------------------------------------------------------------')
    print('Below are the most popular article authors of all time:')
    print('1. ')
    print('2. ')
    print('3. ')
    print('4. ')
    print()

###############################################################################

def answer_q3():
    """On which days did more than 1% of requests lead to errors?"""

    print('Q3---------------------------------------------------------------')
    print(r'On these days more than 1% of requests led to errors:')
    print('1. ')
    print('2. ')
    print('3. ')
    print('4. ')
    print()

###############################################################################

if __name__ == '__main__':
    answer_q1()
    answer_q2()
    answer_q3()
