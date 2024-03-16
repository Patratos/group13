from flask import Blueprint
from flask import render_template, redirect, url_for


# homepage blueprint definition
profile = Blueprint(
    'profile',
    __name__,
    static_folder='static',
    static_url_path='/profile',
    template_folder='templates'
)


# Routes
@profile.route('/profile')
def index():
    return render_template('profile.html')
