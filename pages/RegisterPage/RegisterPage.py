from flask import Blueprint, render_template, url_for

RegisterPage = Blueprint(
    'RegisterPage',
    __name__,
    static_folder='static',
    static_url_path='/RegisterPage',
    template_folder='templates'
)


@RegisterPage.route('/RegisterPage')
def register_page():
    return render_template('RegisterPage.html')
