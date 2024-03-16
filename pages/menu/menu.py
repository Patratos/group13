from flask import render_template
from flask import Blueprint

# about blueprint definition
menu = Blueprint(
    'menu',
    __name__,
    static_folder='static',
    static_url_path='/menu',
    template_folder='templates'
)


# Routes
@menu.route('/menu')
def index():
    return render_template('menu.html')
