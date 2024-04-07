from flask import Blueprint, render_template, request, jsonify
from db_connector import *

# from app import LogoutRequired

RegisterPage = Blueprint(
    'RegisterPage',
    __name__,
    static_folder='static',
    static_url_path='/RegisterPage',
    template_folder='templates'
)


@RegisterPage.route('/RegisterPage', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        email = data.get('email')
        address = data.get('address')
        phone = data.get('phone')
        password = data.get('password')

        exists = user_exists(email)
        if exists:
            return jsonify(success=False, error='User already exists')
        else:
            new_user = {
                "Username": username,
                "Email": email,
                "Address": address,
                "Phone": phone,
                "Password": password
            }
            add_user(new_user)
            return jsonify(success=True)
    else:
        return render_template('RegisterPage.html')
