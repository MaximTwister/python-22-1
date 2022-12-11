import json
from prettytable import PrettyTable

from constants import GEN_DB_FILE


def print_gen_list():
    data: list[dict, ...] = load_generators()
    if data:
        titles = data[0].keys()  # => []
        pt = PrettyTable(titles)
        for gen_dict in data:
            pt.add_row(gen_dict.values())
        print(pt)


def start_gen_work():
    pass


def stop_gen_work():
    pass


def load_generators() -> list[dict, ...]:
    with open(GEN_DB_FILE, 'r') as gen_db:
        serialized_data = gen_db.read()
        if serialized_data:
            data = json.loads(serialized_data)
            print(f"Data from file after deserialization: {data}")
            return data
        else:
            return []


def dump_generators(answers_dict: dict):
    data = load_generators()
    new_dict = {"id": get_id(data)}
    new_dict.update(answers_dict)
    # answers_dict["id"] = get_id(data)
    data.append(new_dict)
    with open(GEN_DB_FILE, 'w') as gen_db:
        serialized_data = json.dumps(data)
        gen_db.write(serialized_data)


def get_id(generators: list[dict, ...]):
    if len(generators) == 0:
        return 1
    else:
        return max([g.get("id") for g in generators]) + 1
