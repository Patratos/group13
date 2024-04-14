from flask import Blueprint, render_template, session, request, jsonify
from db_connector import *

ProfilePage = Blueprint(
    'ProfilePage',
    __name__,
    static_folder='static',
    static_url_path='/ProfilePage',
    template_folder='templates'
)


@ProfilePage.route('/ProfilePage')
def profile_page():
    if not session.get('LoggedIn') is None:  # if a session exists.
        if session != {}:  # if a session isn't empty
            if session['LoggedIn']:  # if in an existing session, the user logged in
                username = session['Username']
                email = session['Email']
                phone = session['Phone']
                address = session['Address']
                return render_template('ProfilePage.html', username=username, email=email, phone=phone, address=address)

            else:
                return render_template('LoginPage.html')
        else:
            return render_template('LoginPage.html')
    else:
        return render_template('LoginPage.html')


@ProfilePage.route('/Logout')
def logout():
    session['LoggedIn'] = False
    return render_template('LoginPage.html')


@ProfilePage.route('/UpdateProfile', methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        data = request.json
        # if the new data is empty, don't update.
        if data.get('username') != "":
            session['Username'] = data.get('username')
        if data.get('email') != "":
            session['Email'] = data.get('email')
        if data.get('address') != "":
            session['Address'] = data.get('address')
        if data.get('phone') != "":
            session['Phone'] = data.get('phone')
        # update the user in the database
        update_user(get_id(session['Email']), session['Username'], session['Email'], session['Address'],
                    session['Phone'])
        return jsonify(success=True)
    else:
        return render_template('ProfilePage.html')
