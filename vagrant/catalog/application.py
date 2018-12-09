#!/usr/bin/python3

###############################################################################
# Item Catalog Application
###############################################################################

from flask import Flask, jsonify, request, render_template, url_for, redirect, flash
from flask import session as login_session
import random
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

###############################################################################


app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json',
                            'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog"

engine = create_engine('sqlite:///itemcatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

###############################################################################
# Routes
###############################################################################


@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase +
                                  string.digits) for _ in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

###############################################################################


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        print(oauth_flow)
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1].decode('utf-8'))
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;' \
              '-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as {:s}".format(login_session['username']))
    print("done!")
    return output

###############################################################################


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is {:s}'.format(access_token))
    print('User name is: ')
    print(login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

###############################################################################


@app.route('/')
def home():
    items = session.query(Item).order_by(Item.id.desc()).all()
    return render_template('all_items.html', items=items)

###############################################################################


@app.route('/items/')
def all_items():
    items = session.query(Item).order_by(Item.id.desc()).all()
    return render_template('all_items.html', items=items)


###############################################################################


@app.route('/items/<int:item_id>/')
def view_item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('view_item.html', item=item)

###############################################################################


@app.route('/items/add/', methods=['GET', 'POST'])
def add_item():
    categories = session.query(Category).order_by(Category.id.desc()).all()
    if request.method == 'POST':
        item = Item(name=request.form['name'],
                    description=request.form['description'],
                    category_id=request.form['category_id'])

        session.add(item)
        session.commit()

        return redirect(url_for('view_item', item_id=item.id))
    else:
        return render_template('add_item.html', categories=categories)

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


@app.route('/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def delete_item(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    category_id = item.category_id

    if request.method == 'POST':
        session.delete(item)
        session.commit()

        return redirect(url_for('view_category',
                                category_id=category_id))
    else:
        return render_template('delete_item.html', item=item)

###############################################################################


@app.route('/categories/')
def all_categories():
    categories = session.query(Category).order_by(Category.id.desc()).all()
    return render_template('all_categories.html', categories=categories)

###############################################################################


@app.route('/categories/<int:category_id>/')
def view_category(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('view_category.html',
                           category=category,
                           items=items)

###############################################################################


@app.route('/categories/add/', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category = Category(name=request.form['name'])
        session.add(category)
        session.commit()

        return redirect(url_for('view_category', category_id=category.id))
    else:
        return render_template('add_category.html')

###############################################################################


@app.route('/categories/<int:category_id>/add/', methods=['GET', 'POST'])
def add_category_item(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        item = Item(name=request.form['name'],
                    description=request.form['description'],
                    category_id=category_id)

        session.add(item)
        session.commit()

        return redirect(url_for('view_item', item_id=item.id))
    else:
        return render_template('add_category_item.html', category=category)

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
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

###############################################################################


if __name__ == '__main__':
    main()

