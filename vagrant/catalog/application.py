#!/usr/bin/python3

###############################################################################
# Item Catalog Application
###############################################################################

from flask import Flask, jsonify, request, render_template, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

###############################################################################


app = Flask(__name__)
engine = create_engine('sqlite:///itemcatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###############################################################################
# Read Routes
###############################################################################


@app.route('/')
def home():
    items = session.query(Item).all()
    return render_template('all_items.html', items=items)

###############################################################################


@app.route('/items/')
def all_items():
    items = session.query(Item).all()
    return render_template('all_items.html', items=items)


###############################################################################


@app.route('/items/<int:item_id>/')
def view_item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('view_item.html', item=item)

###############################################################################


@app.route('/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def edit_item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']

        session.add(item)
        session.commit()

        return redirect(url_for('view_item', item_id=item_id))
    else:
        return render_template('edit_item.html', item=item)


###############################################################################


@app.route('/categories/')
def all_categories():
    categories = session.query(Category).all()
    return render_template('all_categories.html', categories=categories)

###############################################################################


@app.route('/categories/<int:category_id>/')
def view_category(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('view_category.html',
                           category_name=category.name, items=items)

###############################################################################
# API End points
###############################################################################


@app.route('/api/items/')
def all_items_api():
    items = session.query(Item).all()
    return jsonify(Items=[i.serialize for i in items])

###############################################################################


@app.route('/api/items/<int:item_id>/')
def view_item_api(item_id):
    items = session.query(Item).filter_by(id=item_id).all()
    return jsonify(Items=[i.serialize for i in items])

###############################################################################


@app.route('/api/categories/')
def all_categories_api():
    categories = session.query(Category).all()
    return jsonify(Items=[i.serialize for i in categories])

###############################################################################


@app.route('/api/categories/<int:category_id>/')
def view_category_api(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])

###############################################################################


def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

###############################################################################


if __name__ == '__main__':
    main()

