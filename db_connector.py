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


# Create all necessary functions
def user_exists(email):
    return users_col.find_one({'Email': email})


def add_user(user):
    users_col.insert_one(user)


def find_user(email, password):
    return users_col.find_one({'Email': email, 'Password': password})
