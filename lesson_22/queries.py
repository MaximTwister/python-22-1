from datetime import datetime
from pprint import pprint

from no_sql_02 import rooms_coll, room_types


def get_rooms_by_view(view):
    return rooms_coll.find_one({"view": view})


# mountain_view_room = get_rooms_by_view("Mountain View")
# print(type(mountain_view_room), mountain_view_room)


def get_rooms_by_type(room_type):
    return list(rooms_coll.find({"type": room_type}))


# for room_type in room_types:
#     print(f"{room_type} : {len(get_rooms_by_type(room_type))}")

def get_available_rooms_by_date(date):
    return list(
        rooms_coll.find(
            {"booked_periods": {"$not": {"$elemMatch": {
                "start": {"$lte": date},
                "end": {"$gte": date}
            }}}}
        )
    )


# available_rooms = get_available_rooms_by_date(datetime(2023, 12, 31))
# pprint(available_rooms)
# pprint(len(available_rooms))

# search_query = {"view": "Mountain View"}
# set_query = {"$set": {"view": "Building Site View"}}
# rooms_coll.update_many(search_query, set_query)

corporate_start = datetime(2024, 5, 18)
corporate_end = datetime(2024, 5, 20)
corporate_period = {"start": corporate_start, "end": corporate_end}
search_query = {"view": "Building Site View"}
pull_query = {"$pull": {"booked_periods": corporate_period}}
rooms_coll.update_many(search_query, pull_query)


# Relation DBs -> Vertical Scale
# Mongo - > Horizontal Scale
# Datatypes -> Docs -> Coll -> DBs -> NODES -> SHARDS
