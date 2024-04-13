import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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


def add_product_to_cart(email, product_name, quantity):
    # Retrieve the user's cart
    cart = get_cart(email)

    if cart:
        # Check if the product is already in the cart
        product_exists = False
        for product in cart['Products']:
            if product['Product-name'] == product_name:
                product_exists = True
                # Update the quantity of the existing product
                new_quantity = product['Quantity'] + quantity
                carts_col.update_one(
                    {"User": email, "Products.Product-name": product_name},
                    {"$set": {"Products.$.Quantity": new_quantity}}
                )
                message = "Updated quantity for existing product."
                break

        if not product_exists:
            # Product not found, add new product to the cart
            carts_col.update_one(
                {"User": email},
                {"$push": {"Products": {"Product-name": product_name, "Quantity": quantity}}}
            )
            message = "Added new product to cart."

    else:
        # No cart exists, create a new cart with the product
        new_cart = {
            "User": email,
            "Products": [
                {"Product-name": product_name, "Quantity": quantity}
            ]
        }
        carts_col.insert_one(new_cart)
        message = "Created new cart and added product."
        return message


def get_cart_with_details(email):
    # Fetch the user's cart
    cart = carts_col.find_one({"User": email})
    if cart:
        product_details = []
        # Iterate over each product entry in the cart
        for cart_item in cart["Products"]:
            product_name = cart_item["Product-name"]
            # Fetch the product details from the products collection using the product name
            product = products_col.find_one({"name": product_name})
            if product:
                # Ensure the quantity is extracted correctly from the cart_item
                quantity = cart_item["Quantity"]  # This assumes the quantity is stored as previously described
                # Append product details including the correct quantity from the cart
                product_details.append({
                    "name": product_name,
                    "quantity": quantity,
                    "price": product.get("price", {}),  # Default to 0 if price or format is missing
                    "image_path": product.get("image_path", "default.jpg")  # Provide a default image path if missing
                })
                print(product.get("image_path", "default.jpg"))
        cart["Products"] = product_details
    return cart

def update_product_quantity_in_cart(email, product_name, new_quantity):
    """
    Update the quantity of a specific product in the user's cart.

    :param email: The email address of the user (used to identify the correct cart).
    :param product_name: The name of the product to update.
    :param new_quantity: The new quantity for the product.
    """
    # Update the product quantity in the user's cart
    result = carts_col.update_one(
        {"User": email, "Products.Product-name": product_name},
        {"$set": {"Products.$.Quantity": new_quantity}}
    )

    # Check if the update was successful
    if result.modified_count == 1:
        return "Product quantity updated successfully."
    else:
        return "No changes made to the product quantity, check if the product name exists."
