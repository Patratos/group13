from flask import Blueprint, session, redirect, render_template

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
                return render_template('CartPage.html')
            else:
                return redirect('/LoginPage')
        else:
            return redirect('/LoginPage')
    else:
        return redirect('/LoginPage')
