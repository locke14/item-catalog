Project: Logs Analytics
=============

The goal of this project is to create a reporting tool that prints out reports (in plain text) based on the data in this [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

The code is meant to be run in a ```vagrant``` virtual machine. To load the data, ```cd``` into the ```vagrant``` directory with the ```newsdata.sql``` file and run the command ```psql -d news -f newsdata.sql``` to setup the database.

The ```log_analytics.py``` script answers the following 3 questions from the database:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

To get the answers run ```python3 logs_analytics.py```

Output
------

**1) Below are the three most popular articles of all time:**
- "Candidate is jerk, alleges rival" - 338647 views
- "Bears love berries, alleges bear" - 253801 views
- "Bad things gone, say good people" - 170098 views

**2) Below are the most popular article authors of all time:**
- Ursula La Multa - 507594 views
- Rudolf von Treppenwitz - 423457 views
- Anonymous Contributor - 170098 views
- Markoff Chaney - 84557 views

**3) Below are days where > 1% requests lead to errors:**
- July 17, 2016 - 2.26% errors
