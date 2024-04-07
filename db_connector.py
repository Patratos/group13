import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))

try:
    cluster.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# get all dbs and collections that needed
mydatabase = cluster['KnitSkit']
users_col = mydatabase['users']
products_col = mydatabase['products']
carts_col = mydatabase['carts']


#def fetch_all_products():
#    try:
#        products = products_col.find()
#        for product in products:
#            print(product)
#    except Exception as e:
#        print(f"An error occurred: {e}")


# Call the function to fetch and print all products
#fetch_all_products()


# Create all necessary functions
def get_id(email):
    return users_col.find_one({'Email': email})["_id"]


def user_exists(email):
    return users_col.find_one({'Email': email})


def add_user(user):
    users_col.insert_one(user)


def find_user(email, password):
    return users_col.find_one({'Email': email, 'Password': password})


def update_user(user_id, username, email, address, phone):
    return users_col.update_one({"_id": user_id},
                                {'$set': {'Username': username, 'Email': email, 'Address': address, 'Phone': phone}})

def get_cart(email):
    cart = carts_col.find_one({"User": email})
    print(f"Queried cart for {email}: {cart}")
    return cart

def create_new_cart(email, product_name, quantity):
    new_cart = {
        "User": email,
        "Products": [
            {
                "Product-name": product_name,
                "Quantity": quantity
            }
        ]
    }
    carts_col.insert_one(new_cart)
def add_product_to_cart(email, product_name, quantity):
    # Find the cart document for the user and add a new product to the 'products' array
    carts_col.update_one(
        {"User": email},
        {"$push": {"Products": {"Product-name": product_name, "Quantity": quantity}}}
    )




