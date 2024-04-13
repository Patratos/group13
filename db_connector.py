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
    cart = carts_col.find_one({"User": email})
    if cart:
        product_details = []
        for cart_item in cart["Products"]:
            product_name = cart_item["Product-name"]
            product = products_col.find_one({"name": product_name})
            if product:
                product_details.append({
                    "name": product_name,
                    "quantity": cart_item["Quantity"],
                    "price": product.get("price", 0),  # Default to 0 if price is missing
                    "image_path": product.get("image_path", "default.jpg"),  # Default image if missing
                    "_id": str(product.get("_id"))  # Convert ObjectId to string
                })
        cart["Products"] = product_details
    return cart


def update_cart_items(email, updated_items):
    """
    Updates the quantities of multiple items in the user's cart.

    :param email: Email of the user whose cart is to be updated.
    :param updated_items: List of dictionaries, each containing 'Product-name' and 'Quantity'.
    :return: List of messages indicating the success or failure of each update.
    """
    messages = []
    for item in updated_items:
        product_name = item['Product-name']
        new_quantity = item['Quantity']

        # Perform the update
        if new_quantity > 0:
            result = carts_col.update_one(
                {"User": email, "Products.Product-name": product_name},
                {"$set": {"Products.$.Quantity": new_quantity}}
            )
            # Check the result and create a message accordingly
            if result.modified_count == 1:
                messages.append(f"Quantity for {product_name} updated successfully.")
            else:
                messages.append(
                    f"No changes made to the quantity of {product_name}. Check if the product name exists in the cart.")
        else:
            # If the quantity is zero or less, assume item needs to be removed
            result = carts_col.update_one(
                {"User": email},
                {"$pull": {"Products": {"Product-name": product_name}}}
            )
            if result.modified_count == 1:
                messages.append(f"Removed {product_name} from cart successfully.")
            else:
                messages.append(f"Failed to remove {product_name} from cart. It may not exist.")

    return messages


def remove_item_from_cart(email, product_name):
    """
    Removes an item from the cart based on the user's email and product name.

    :param email: The email address of the user whose cart needs modification.
    :param product_name: The name of the product to remove from the cart.
    :return: A message indicating whether the removal was successful.
    """
    # Attempt to update the cart document by pulling the product from the Products array
    result = carts_col.update_one(
        {"User": email},
        {"$pull": {"Products": {"Product-name": product_name}}}
    )

    if result.modified_count == 1:
        return f"Removed {product_name} from cart successfully."
    else:
        return f"Failed to remove {product_name} from cart. It may not exist."


# Assuming that you already have the necessary imports and MongoDB connection setup

def delete_user_cart(email):
    """
    Deletes the user's cart from the database.

    :param email: Email of the user whose cart is to be deleted.
    :return: A message indicating the result of the operation.
    """
    result = carts_col.delete_one({'User': email})
    if result.deleted_count == 1:
        print(f"Cart for {email} was successfully deleted.")
        return "Cart successfully deleted."
    else:
        print(f"No cart found for {email} to delete.")
        return "No cart found to delete."
