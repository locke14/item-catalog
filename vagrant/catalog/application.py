#!/usr/bin/python3

###############################################################################
# Product Catalog Application
###############################################################################

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Product

###############################################################################


app = Flask(__name__)
engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###############################################################################


@app.route('/')
def home():
    return "This is the home page"

###############################################################################


def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

###############################################################################


if __name__ == '__main__':
    main()

