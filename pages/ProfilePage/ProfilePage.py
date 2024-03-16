from flask import Blueprint, render_template, url_for

ProfilePage = Blueprint(
    'ProfilePage',
    __name__,
    static_folder='static',
    static_url_path='/ProfilePage',
    template_folder='templates'
)


@ProfilePage.route('/ProfilePage')
def profile_page():
    return render_template('ProfilePage.html')
