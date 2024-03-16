from flask import Blueprint, render_template, url_for

LoginPage = Blueprint(
    'LoginPage',
    __name__,
    static_folder='static',
    static_url_path='/LoginPage',
    template_folder='templates'
)


@LoginPage.route('/LoginPage')
def login_page():
    return render_template('LoginPage.html')
