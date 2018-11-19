Project: Logs Analytics
=============

The goal of this project is to create a reporting tool that prints out reports (in plain text) based on the data in this [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

The code is meant to be run context of a ```vagrant``` virtual machine. To load the data, ```cd```into the ```vagrant``` directory with the ```newsdata.sql``` file and use the command ```psql -d news -f newsdata.sql```.

We want to answer the following 3 questions from the database:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?
