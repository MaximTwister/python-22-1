from messages import (
    MAIN_MENU,
    MAIN_MENU_MAP
)

from constants import GEN_KEYS
from utils import dump_generators

show_next_menu = False
main_menu_opt_int = 0

# TODO: rewrite to be flexible with all menus
while show_next_menu is False:
    menu_opt_str = input(MAIN_MENU)
    try:
        menu_opt_int = int(menu_opt_str)
    except ValueError as e:
        print(f"error: unsupported param: {menu_opt_str}")
    else:
        show_next_menu = True


next_object = MAIN_MENU_MAP.get(menu_opt_int, 0)
next_func = next_object.get("func")
next_menu = next_object.get("sub_menu")

if next_func:
    next_func()
else:
    answers = []
    for question in next_menu:
        answer = input(question)
        answers.append(answer)

    answers_dict = dict(zip(GEN_KEYS, answers))
    dump_generators(answers_dict)
