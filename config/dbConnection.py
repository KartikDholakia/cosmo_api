from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

config = dotenv_values(".env")

# Create a new client and connect to the server
client = MongoClient(config["MONGODB_CONNECTION_URI"], server_api=ServerApi('1'))
