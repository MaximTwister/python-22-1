import json
import time
from typing import Callable

from prettytable import PrettyTable

from constants import (
    GEN_DB_FILE,
    GEN_KEYS,
    EMPTY_SESSION,
    WORKING,
    STOPPED,
    GOOD,
    MAINTENANCE,
    MAIN_MENU_OPTION,
    LIST_GEN_MENU_OPTION,
    TABLE_TITLES,
)
from messages import (
    MAIN_MENU,
    UNSUPPORTED_PARAM_TEMPLATE,
    CHOOSE_GEN_TEMPLATE,
    NEW_GEN_QUIZ,
)


def print_gen_list(filter_func: Callable = None):
    data: list[dict] = load_generators()
    if data:
        if filter_func:
            data = filter_func(data)
        pt = PrettyTable(TABLE_TITLES)
        for gen in data:
            pt.add_row([gen.get(key) for key in TABLE_TITLES])
        print(pt.get_string(fields=TABLE_TITLES))
    return MAIN_MENU_OPTION


def select_gen_menu(filter_func: Callable, state: str):
    print_gen_list(filter_func)
    gen_id = input(CHOOSE_GEN_TEMPLATE.format(state=state))
    if gen_id.isdigit():
        return int(gen_id)
    else:
        print(UNSUPPORTED_PARAM_TEMPLATE.format(param=gen_id))


def filter_stopped_gens(data):
    return [gen for gen in data if gen["state"] == STOPPED]


def filter_started_gens(data):
    return [gen for gen in data if gen["state"] == WORKING]


def filter_maintainable_gens(data):
    return [gen for gen in data if gen["oil"] == MAINTENANCE]


def start_gen_work():
    gen_id = select_gen_menu(filter_func=filter_stopped_gens, state="start")
    data = load_generators()
    for gen in data:
        if gen["id"] == gen_id:
            gen["state"] = WORKING
            gen["session"]["start"] = time.time()
    dump_generators(data)
    return LIST_GEN_MENU_OPTION


def stop_gen_work():
    gen_id = select_gen_menu(filter_func=filter_started_gens, state="stop")
    data = load_generators()
    for gen in data:
        if gen["id"] == gen_id:
            gen["state"] = STOPPED
            gen["session"]["stop"] = time.time()
            calculate_motohours(gen)
            notify(gen)
    dump_generators(data)
    return LIST_GEN_MENU_OPTION


def calculate_motohours(gen):
    session_delta_seconds = gen["session"]["stop"] - gen["session"]["start"]
    gen["motohours"] += round(session_delta_seconds / 3600, 3)
    gen["session"] = EMPTY_SESSION


def notify(gen):
    if gen["motohours"] >= gen["change_oil_period"]:
        gen["oil"] = MAINTENANCE


def load_generators() -> list[dict, ...]:
    data = []
    with open(GEN_DB_FILE, 'r') as gen_db:
        serialized_data = gen_db.read()
        if serialized_data:
            data = json.loads(serialized_data)
    return data


def dump_generators(data: list[dict]):
    with open(GEN_DB_FILE, 'w') as gen_db:
        serialized_data = json.dumps(data)
        gen_db.write(serialized_data)


def get_id(generators: list[dict, ...]):
    if len(generators) == 0:
        return 1
    else:
        return max([g.get("id") for g in generators]) + 1


def add_gen():
    answers = []
    for question in NEW_GEN_QUIZ:
        answer = input(question)
        answers.append(answer)

    data = load_generators()
    gen = dict(zip(GEN_KEYS, answers))
    gen["id"] = get_id(data)
    gen["change_oil_period"] = int(gen["change_oil_period"])
    gen["session"] = EMPTY_SESSION
    gen["motohours"] = 0
    gen["state"] = STOPPED
    gen["oil"] = GOOD
    data.append(gen)
    dump_generators(data)

    return MAIN_MENU_OPTION


def show_main_menu():
    param = input(MAIN_MENU)
    try:
        param_int = int(param)
    except ValueError as e:
        print(UNSUPPORTED_PARAM_TEMPLATE.format(param=param))
        show_main_menu()
    else:
        return param_int


def perform_maintenance():
    gen_id = select_gen_menu(filter_func=filter_maintainable_gens, state="maintain")
    data = load_generators()
    for gen in data:
        if gen["id"] == gen_id:
            gen["motohours"] = 0.000
            gen["oil"] = GOOD
    dump_generators(data)
    return LIST_GEN_MENU_OPTION
