from db_connector import users_col, products_col, carts_col


def analyze_users():
    print("Customers collection:")
    for user in users_col.find():
        print(user)
    print()


def analyze_products():
    print("Products collection:")
    for product in products_col.find():
        print(product)
    print()


def analyze_carts():
    print("Products collection:")
    for cart in carts_col.find():
        print(cart)
    print()


# Call all analyzer functions of collections in database
def main():
    print("DB Collections:")
    analyze_users()
    analyze_products()
    analyze_carts()


if __name__ == "__main__":
    main()
