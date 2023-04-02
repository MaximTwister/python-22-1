from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne
from pymongo.errors import BulkWriteError
from datetime import datetime
import pymongo
import pprint
from faker import Faker
from provider import brands_provider, price_provider

client = pymongo.MongoClient("mongodb+srv://tatmika:student2023@cluster0.sxdh6sk.mongodb.net/")
print(client)

db = client["insurance_db"]
contracts_collection = db["contracts"]

fkr = Faker("uk_UA")
fkr.add_provider(brands_provider)
fkr.add_provider(price_provider)


def create_contracts():
    return {
        "form": fkr.bothify(text='????-########', letters='ABCDE'),
        "date_contract": fkr.date_time_between(start_date='-2y', end_date='now'),
        "name": fkr.name(),
        "car_brand": fkr.car_brands(),
        "car_reg_number": fkr.license_plate(),
        "color": fkr.safe_color_name(),
        "email": fkr.email(),
        "phone_number": fkr.phone_number(),
        "price": fkr.price()
    }


for _ in range(10):
    contract = create_contracts()
    contracts_collection.insert_one(contract)

# Total number of insurance policies
count = contracts_collection.count_documents({})
print(f"Total number of insurance policies before bulk_write(): {count}")

# Toyota insurance policy example
toyota = contracts_collection.find_one({"car_brand": "Toyota"})
pprint.pprint(f"Toyota insurance policy example: {toyota}")

requests = [
    DeleteMany({"date_contract": {'$lt': "2022-04-01"}}),
    # DeleteMany({}),
    InsertOne(
        {"form": "AAAA-1212121", "date_contract": "2023-04-02", "name": "Віктор Резник", "car_brand": "Opel",
         "car_reg_number": "TT 5489 AA", "color": "white", "email": "ttt@i.ua",
         "phone_number": "050-55-55-555", "price": 1500}),
    InsertOne(
        {"form": "AAAA-1212121", "date_contract": "2023-04-02", "name": "Олександр Липовой", "car_brand": "Opel",
         "car_reg_number": "TT 0102 AA", "color": "white", "email": "ttt@i.ua",
         "phone_number": "050-55-55-555", "price": 1500}),
    InsertOne(
        {"form": "BBBB-8888885", "date_contract": "2023-04-02", "name": "Олена Хоменко", "car_brand": "BMW",
         "car_reg_number": "TT 1234 AA", "color": "red", "email": "uuu@i.ua", "phone_number": "050-55-55-000",
         "price": 2500}),
    UpdateOne({"_form": "BBBB-8888885"}, {'$set': {"color": "grey"}}),

    UpdateOne({"_form": "AAAA-1212121"}, {'$inc': {'price': 500}}, upsert=True)

]

try:
    db.contracts.bulk_write(requests)  # type: ignore
except BulkWriteError as bwe:
    print(bwe.details)



# Total number of insurance policies
count_after = contracts_collection.count_documents({})
print(f"Total number of insurance policies after bulk_write(): {count_after}")
