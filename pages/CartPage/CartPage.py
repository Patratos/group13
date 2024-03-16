from flask import Blueprint, render_template, url_for

CartPage = Blueprint(
    'CartPage',
    __name__,
    static_folder='static',
    static_url_path='/CartPage',
    template_folder='templates'
)


@CartPage.route('/CartPage')
def cart_page():
    return render_template('CartPage.html')
