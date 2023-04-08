from datetime import datetime

import pymongo
from faker import Faker


client = pymongo.MongoClient("mongodb+srv://twister:twister00@cluster0.v3tkkdi.mongodb.net")

print(f"client: {client}")
db = client["test_db"]
users_collection = db["users"]

fkr = Faker()


def create_user():
    return {
        "name": fkr.name(),
        "email": fkr.email(),
        "created_at": datetime.now()
    }


# for _ in range(10):
#     user = create_user()
#     users_collection.insert_one(user)
