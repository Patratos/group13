from bson.objectid import ObjectId
from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify, current_app, session
from flask_login import current_user
from db_connector import *
import logging
from app import *
HomePage = Blueprint(
    'HomePage',
    __name__,
    static_folder='static',
    static_url_path='/HomePage',
    template_folder='templates'
)


@HomePage.route('/')
@HomePage.route('/HomePage')
def home_page():
    products = list(products_col.find({}, {'_id': 0}))
    return render_template('HomePage.html', products=products)

@HomePage.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    if not session.get('LoggedIn'):
        app.logger.info('Info level log')
        app.logger.warning('Warning level log')
        flash('User not logged in.', 'error')
        return jsonify({'error': 'User not logged in.'}), 401

    user = get_id(session.get('Email'))
    email = session.get('Email')
    print(f"Email from session: {email}")
    product_id = data.get('product_id')
    product_name = data.get('product_name')  # Corrected key name
    quantity = int(data.get('quantity', 1))
    print(f" Converted this item: {product_id}, {product_name}, {quantity}")  # Debug print

    # checking if the user already has a cart
    cart = get_cart(email)

    # if the user has a cart update it else create a new cart for the user
    if cart:
        add_product_to_cart(email, product_id, quantity)
        print("adding to cart in python")
        flash('Python added an item successfully.', 'success')
    else:
        create_new_cart(email, product_name, quantity)
        print("creating a cart in python")
        flash('python created a cart and added an item successfully.', 'success')

    return jsonify(success=True)

