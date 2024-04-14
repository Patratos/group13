from flask import Blueprint, session, redirect, render_template, flash, url_for, request, jsonify
from db_connector import *  # Ensure db_connector has all the necessary functions

CartPage = Blueprint(
    'CartPage',
    __name__,
    static_folder='static',
    static_url_path='/CartPage',
    template_folder='templates'
)


@CartPage.route('/CartPage', methods=['GET', 'POST'])
def cart_page():
    if not session.get('LoggedIn'):
        return redirect(url_for('LoginPage.login_page'))

    email = session.get('Email')
    if request.method == 'POST':
        try:
            updated_items = request.json['items']
            messages = update_cart_items(email, updated_items)
            return jsonify({'success': True, 'messages': messages})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})

    cart = get_cart_with_details(email)
    items = cart['Products'] if cart else []
    return render_template('CartPage.html', items=items)


def update_cart_items(email, updated_items):
    """
    Updates the quantities of multiple items in the user's cart or removes them.

    :param email: Email of the user whose cart is to be updated.
    :param updated_items: List of dictionaries, each containing 'Product-name' and 'Quantity'.
    :return: List of messages indicating the success or failure of each update.
    """
    messages = []
    for item in updated_items:
        product_name = item['Product-name']
        new_quantity = item['Quantity']

        if new_quantity > 0:
            result = carts_col.update_one(
                {"User": email, "Products.Product-name": product_name},
                {"$set": {"Products.$.Quantity": new_quantity}}
            )
            if result.modified_count == 1:
                messages.append(f"Quantity for {product_name} updated successfully.")
            else:
                messages.append(
                    f"No changes made to the quantity of {product_name}. Check if the product name exists in the cart.")
        else:
            result = carts_col.update_one(
                {"User": email},
                {"$pull": {"Products": {"Product-name": product_name}}}
            )
            if result.modified_count == 1:
                messages.append(f"Removed {product_name} from cart successfully.")
            else:
                messages.append(f"Failed to remove {product_name} from cart. It may not exist.")

    return messages


def get_cart_with_details(email):
    """
    Fetches detailed information about the user's cart, including product details.
    """
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
                    "price": product.get("price", 0),
                    "image_path": product.get("image_path", "default.jpg"),
                    "_id": str(product["_id"])
                })
        cart["Products"] = product_details
    return cart


@CartPage.route('/CartPage/remove', methods=['POST'])
def remove_item():
    if not session.get('LoggedIn'):
        return jsonify({'success': False, 'message': 'Login required'}), 401

    email = session.get('Email')
    product_name = request.json.get('Product-name')
    message = remove_item_from_cart(email, product_name)

    if "successfully" in message:
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'message': message})
