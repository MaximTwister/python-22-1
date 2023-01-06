import sys

from messages import UNSUPPORTED_PARAM_TEMPLATE

from utils import (
    show_main_menu,
    add_gen,
    print_gen_list,
    start_gen_work,
    stop_gen_work,
    perform_maintenance,
)


MAIN_MENU_MAP = {
    0: show_main_menu,
    1: add_gen,
    2: print_gen_list,
    3: start_gen_work,
    4: stop_gen_work,
    5: perform_maintenance,
    6: sys.exit
}


def main():
    param = show_main_menu()
    while True:
        next_func = MAIN_MENU_MAP.get(param, None)
        if next_func:
            param = next_func()
        else:
            print(UNSUPPORTED_PARAM_TEMPLATE.format(param=param))
            param = show_main_menu()

main()
