from flask import Blueprint
from flask import render_template, redirect, url_for


# homepage blueprint definition
homepage = Blueprint(
    'homepage',
    __name__,
    static_folder='static',
    static_url_path='/homepage',
    template_folder='templates'
)


# Routes
@homepage.route('/')
def index():
    return render_template('homepage.html')


@homepage.route('/homepage')
@homepage.route('/home')
def redirect_homepage():
    # print('I am in /Homepage route!')
    return redirect(url_for('homepage.index'))
