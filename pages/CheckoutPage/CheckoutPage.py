from flask import Blueprint, render_template, session, redirect, flash, jsonify, request
from db_connector import *
CheckoutPage = Blueprint(
    'CheckoutPage',
    __name__,
    static_folder='static',
    static_url_path='/CheckoutPage',
    template_folder='templates'
)


@CheckoutPage.route('/CheckoutPage')
def checkout_page():
    phone = session['Phone']
    address = session['Address']
    if address == '' or phone == '':
        flash('Missing address and phone number', 'attention')
        return redirect('/ProfilePage')
    else:
        return render_template('CheckoutPage.html')

@CheckoutPage.route('/CheckoutPage/confirmPayment', methods=['POST'])
@CheckoutPage.route('/CheckoutPage/confirmPayment', methods=['POST'])
def confirm_payment():
    if not session.get('LoggedIn'):
        return jsonify({'success': False, 'message': 'User must be logged in to complete payment.'}), 401

    data = request.get_json()
    creditCard = data.get('creditCard')
    expiryDate = data.get('expiryDate')
    cvv = data.get('cvv')

    # Assume basic validation is already done, here just for demonstration
    if len(creditCard) == 16 and "/" in expiryDate and len(cvv) == 3:
        email = session.get('Email')
        message = delete_user_cart(email)  # Delete the user's cart after confirming payment
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'message': 'Invalid payment details provided.'})