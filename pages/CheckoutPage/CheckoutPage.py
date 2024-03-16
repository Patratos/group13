from flask import Blueprint, render_template, url_for

CheckoutPage = Blueprint(
    'CheckoutPage',
    __name__,
    static_folder='static',
    static_url_path='/CheckoutPage',
    template_folder='templates'
)


@CheckoutPage.route('/CheckoutPage')
def checkout_page():
    return render_template('CheckoutPage.html')
