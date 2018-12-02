#!/usr/bin/python3

###############################################################################
# Product Catalog Application
###############################################################################

from flask import Flask, jsonify, request, render_template, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Product

###############################################################################


app = Flask(__name__)
engine = create_engine('sqlite:///productcatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###############################################################################
# Read Routes
###############################################################################


@app.route('/')
def home():
    products = session.query(Product).all()
    return render_template('all_products.html', products=products)

###############################################################################


@app.route('/products/')
def all_products():
    products = session.query(Product).all()
    return render_template('all_products.html', products=products)


###############################################################################


@app.route('/products/<int:product_id>/')
def view_product(product_id):
    product = session.query(Product).filter_by(id=product_id).one()
    return render_template('view_product.html', product=product)

###############################################################################


@app.route('/products/<int:product_id>/edit/', methods=['GET', 'POST'])
def edit_product(product_id):
    product = session.query(Product).filter_by(id=product_id).one()
    if request.method == 'POST':
        if request.form['name']:
            product.name = request.form['name']
            return redirect(url_for('view_product', product_id=product_id))
    else:
        return render_template('edit_product.html', product=product)


###############################################################################


@app.route('/categories/')
def all_categories():
    categories = session.query(Category).all()
    return render_template('all_categories.html', categories=categories)

###############################################################################


@app.route('/categories/<int:category_id>/')
def view_category(category_id):
    products = session.query(Product).filter_by(category_id=category_id).all()
    return render_template('view_category.html',
                           category_id=category_id, products=products)

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

