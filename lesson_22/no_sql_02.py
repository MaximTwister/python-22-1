import os
from datetime import datetime, timedelta
from pprint import pprint
from random import choice, randint

from pymongo import MongoClient

mongo_login = os.environ.get("MONGO_LOGIN")
mongo_pass = os.environ.get("MONGO_PASS")
mongo_uri = f"mongodb+srv://{mongo_login}:{mongo_pass}@cluster0.v3tkkdi.mongodb.net"

client = MongoClient(mongo_uri)
db = client["hotel"]
rooms_coll = db["rooms"]

room_types = ["Single", "Double", "Studio", "Suite"]
room_views = ["Mountain View", "Sea View"]


def random_date_periods(start_date, end_date, amount):
    booked_date_periods = []
    for _ in range(amount):
        days = (end_date - start_date).days
        start = start_date + timedelta(days=randint(0, days))
        end = start + timedelta(days=randint(1, 14))
        booked_date_periods.append({"start": start, "end": end})
    return booked_date_periods


def generate_rooms(amount):
    rooms = []
    for _ in range(amount):
        room_type = choice(room_types)
        beds = 1 if room_type == "Single" else 2
        room_view = choice(room_views)
        booked_periods = random_date_periods(
            datetime(2023, 1, 1),
            datetime(2023, 12, 31),
            randint(1, 20)
        )
        room = {
            "type": room_type,
            "beds": beds,
            "view": room_view,
            "booked_periods": booked_periods
        }

        rooms.append(room)
    return rooms


def insert_rooms(rooms: list[dict]):
    res = rooms_coll.insert_many(rooms)
    print(f"Inserted {len(res.inserted_ids)} rooms into `rooms` collection.")


if __name__ == "__main__":
    generated_rooms = generate_rooms(100)
    insert_rooms(generated_rooms)
