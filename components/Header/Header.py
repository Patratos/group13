from flask import Blueprint, render_template, url_for

Header = Blueprint(
    'Header',
    __name__,
    static_folder='static',
    static_url_path='/Header',
    template_folder='templates'
)


@Header.route('/Header')
def header_part():
    return render_template('Header.html')
