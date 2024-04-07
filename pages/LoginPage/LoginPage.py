from flask import Blueprint, render_template, request, session, jsonify
from db_connector import *

LoginPage = Blueprint(
    'LoginPage',
    __name__,
    static_folder='static',
    static_url_path='/LoginPage',
    template_folder='templates'
)


@LoginPage.route('/LoginPage', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user = find_user(email, password)

        if user:
            session['Email'] = email
            session['Password'] = password
            session['Username'] = user.get('Username')
            session['Phone'] = user.get('Phone')
            session['Address'] = user.get('Address')
            session['LoggedIn'] = True
            return jsonify(success=True)

        else:
            exists = user_exists(email)
            if exists:
                return jsonify(success=False, error="Incorrect password")
            else:
                return jsonify(success=False, error="User not found")
    else:
        return render_template('LoginPage.html')
