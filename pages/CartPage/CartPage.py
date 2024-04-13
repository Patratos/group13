from flask import Blueprint, session, redirect, render_template, flash, url_for,request, jsonify
from db_connector import *

CartPage = Blueprint(
    'CartPage',
    __name__,
    static_folder='static',
    static_url_path='/CartPage',
    template_folder='templates'
)

@CartPage.route('/CartPage', methods=['GET', 'POST'])
def cart_page():
    if not session.get('LoggedIn'):
        flash('You need to login to view your cart', 'error')
        return redirect(url_for('LoginPage.login_page'))

    email = session.get('Email')
    if request.method == 'POST':
        updated_items = request.json['items']
        messages = []
        for item in updated_items:
            result_message = update_product_quantity_in_cart(email, item['Product-name'], item['Quantity'])
            messages.append(result_message)
        return jsonify({'success': True, 'messages': messages})

    cart = get_cart_with_details(email)
    items = cart['Products'] if cart else []
    return render_template('CartPage.html', items=items)

def update_cart_items(email, updated_items):
    # Logic to update the cart in the database based on the provided item updates
    for item in updated_items:
        # Assuming each item contains 'id', 'quantity'
        update_product_quantity_in_cart(email, item['id'], item['quantity'])
    return get_cart_with_details(email)
