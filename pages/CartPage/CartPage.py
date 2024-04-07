from flask import Blueprint, render_template, url_for, request, redirect, flash, jsonify
from flask_login import current_user
from db_connector import *
from bson.objectid import ObjectId

CartPage = Blueprint(
    'CartPage',
    __name__,
    static_folder='static',
    static_url_path='/CartPage',
    template_folder='templates'
)


@CartPage.route('/CartPage')
def cart_page():
    user_id = current_user.id()
    cart = mydatabase.carts.find_one({"Email": ObjectId(user_id)})
    if cart is None:
        cart_items = []
    else:
        cart_items = []
        for product in cart['products']:
            product = mydatabase.products.find_one({"name": product['name']})
            if product:
                cart_items.append({
                    "name": product['name'],
                    "price": product['price'],
                    "quantity": product['quantity'],

                })

    return render_template('CartPage.html', cart_items=cart_items)
