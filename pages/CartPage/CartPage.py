from flask import Blueprint, session, redirect, render_template, flash, url_for
from db_connector import *

CartPage = Blueprint(
    'CartPage',
    __name__,
    static_folder='static',
    static_url_path='/CartPage',
    template_folder='templates'
)


@CartPage.route('/CartPage')
def cart_page():
    if not session.get('LoggedIn') is None:  # if a session exists.
        if session != {}:  # if a session isn't empty
            if session['LoggedIn']:  # if in an existing session, the user logged in
                email = session.get('Email')
                cart = get_cart(email)
                if cart:
                    items = cart['Products']
                else:
                    items = []
                return render_template('CartPage.html', items=items)
            else:
                flash('You need to login to view your cart', 'error')
                return redirect(url_for('LoginPage.login_page'))
        else:
            return redirect('/LoginPage')
    else:
        return redirect('/LoginPage')
