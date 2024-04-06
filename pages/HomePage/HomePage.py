from flask import Blueprint, render_template, url_for
from db_connector import *

HomePage = Blueprint(
    'HomePage',
    __name__,
    static_folder='static',
    static_url_path='/HomePage',
    template_folder='templates'
)


@HomePage.route('/')
@HomePage.route('/HomePage')
def home_page():
    products = list(products_col.find({}, {'_id': 0}))
    return render_template('HomePage.html', products=products)
