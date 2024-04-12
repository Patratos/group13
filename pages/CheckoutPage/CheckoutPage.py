from flask import Blueprint, render_template, session, redirect

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
        return redirect('/ProfilePage')
    else:
        return render_template('CheckoutPage.html')
        # return redirect('/CheckoutPage')
