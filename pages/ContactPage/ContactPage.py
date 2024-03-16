from flask import Blueprint, render_template, url_for

ContactPage = Blueprint(
    'ContactPage',
    __name__,
    static_folder='static',
    static_url_path='/ContactPage',
    template_folder='templates'
)


@ContactPage.route('/ContactPage')
def contact_page():
    return render_template('ContactPage.html')
