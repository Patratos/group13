from flask import Flask

# App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

# Pages
# Home page
from pages.HomePage.HomePage import HomePage

app.register_blueprint(HomePage)

# Cart page
from pages.CartPage.CartPage import CartPage

app.register_blueprint(CartPage)

# Checkout Page
from pages.CheckoutPage.CheckoutPage import CheckoutPage

app.register_blueprint(CheckoutPage)

# Contact Page
from pages.ContactPage.ContactPage import ContactPage

app.register_blueprint(ContactPage)

# Login Page
from pages.LoginPage.LoginPage import LoginPage

app.register_blueprint(LoginPage)

# Profile Page
from pages.ProfilePage.ProfilePage import ProfilePage

app.register_blueprint(ProfilePage)

# Register Page
from pages.RegisterPage.RegisterPage import RegisterPage

app.register_blueprint(RegisterPage)

# Components

# Header Component
from components.Header.Header import Header

app.register_blueprint(Header)

# Footer Component
from components.Footer.Footer import Footer

app.register_blueprint(Footer)
