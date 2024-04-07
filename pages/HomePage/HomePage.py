from flask import Blueprint, render_template, request, session, jsonify, flash
from db_connector import *

HomePage = Blueprint(
    'HomePage',
    __name__,
    static_folder='static',
    static_url_path='/HomePage',
    template_folder='templates'
)


@HomePage.route('/')
@HomePage.route('/HomePage', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        # def add_to_cart():
        data = request.json
        if not session.get('LoggedIn'):
            flash('User not logged in.', 'error')
            return jsonify({'error': 'User not logged in.'}), 401

        email = session.get('Email')
        print(f"Email from session: {email}")
        product_id = data.get('product_id')
        product_name = data.get('product_name')  # Corrected key name
        quantity = int(data.get('quantity', 1))
        print(f" Converted this item: {product_id}, {product_name}, {quantity}")  # Debug print
        add_product_to_cart(email, product_id, quantity)

        return jsonify(success=True)
    else:
        products = list(products_col.find({}, {'_id': 0}))
        return render_template('HomePage.html', products=products)
