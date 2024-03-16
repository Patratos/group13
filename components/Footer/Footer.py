from flask import Blueprint, render_template, url_for

Footer = Blueprint(
    'Footer',
    __name__,
    static_folder='static',
    static_url_path='/Footer',
    template_folder='templates'
)


@Footer.route('/Footer')
def footer_part():
    return render_template('Footer.html')
