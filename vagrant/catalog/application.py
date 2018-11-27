#!/usr/bin/python3

###############################################################################
# Product Catalog Application
###############################################################################

from flask import Flask, jsonify
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
# Read Routes
###############################################################################


@app.route('/')
@app.route('/products/')
def all_products():
    products = session.query(Product).all()
    output = ''
    for i in products:
        output += i.name
        output += '</br>'
        output += str(i.id)
        output += '</br>'
    return output


###############################################################################


@app.route('/products/<int:product_id>/')
def view_product(product_id):
    products = session.query(Product).filter_by(id=product_id).all()
    print(products)
    output = ''
    for i in products:
        output += i.name
        output += '</br>'
        output += i.description
    return output

###############################################################################


@app.route('/categories/')
def all_categories():
    categories = session.query(Category).all()
    output = ''
    for i in categories:
        output += i.name
        output += '</br>'
    return output

###############################################################################


@app.route('/categories/<int:category_id>/')
def view_category(category_id):
    products = session.query(Product).filter_by(category_id=category_id).all()
    output = ''
    for i in products:
        output += i.name
        output += '</br>'
    return output

###############################################################################
# API End points
###############################################################################


@app.route('/api/products/')
def all_products_api():
    products = session.query(Product).all()
    return jsonify(Products=[i.serialize for i in products])

###############################################################################


@app.route('/api/products/<int:product_id>/')
def view_product_api(product_id):
    products = session.query(Product).filter_by(id=product_id).all()
    return jsonify(Products=[i.serialize for i in products])

###############################################################################


@app.route('/api/categories/')
def all_categories_api():
    categories = session.query(Category).all()
    return jsonify(Products=[i.serialize for i in categories])

###############################################################################


@app.route('/api/categories/<int:category_id>/')
def view_category_api(category_id):
    products = session.query(Product).filter_by(category_id=category_id).all()
    return jsonify(Products=[i.serialize for i in products])


###############################################################################


def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

###############################################################################


if __name__ == '__main__':
    main()

