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
accounts_col = mydatabase['accounts']

new_account = {
    'name': 'admin',
    'password': '<PASSWORD>',
    'email': 'admin@admin.com',
    'phone': '0365937628'
}
accounts_col.insert_one(new_account)

# # create all necessary functions
# def get_list_of_customers():
#     return list(customers_col.find())
# def insert_customer(customer_dict):
#     customers_col.insert_one(customer_dict)
# ...
