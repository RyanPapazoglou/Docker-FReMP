import os
from pymongo import MongoClient
# for now we use local: 'mongodb://127.0.0.1:27017' with DB: 'testdb'


# database = os.getenv("MONGODB")
database = 'mongodb://127.0.0.1:27017'
client = MongoClient()
db = client.testdb