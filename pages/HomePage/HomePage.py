from flask import Blueprint, render_template, url_for

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
    return render_template('HomePage.html')
