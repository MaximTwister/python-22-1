from utils import (
    print_gen_list,
    start_gen_work,
    stop_gen_work,
)

MAIN_MENU = "1. Add new generator\n" \
            "2. List generators\n" \
            "3. Start\n" \
            "4. Stop\n" \
            "5. Exit\n" \
            "Select menu option: "

NEW_GEN_NAME = "1.1 Enter generator name: "
NEW_GEN_DESCR = "1.2 Enter generator description: "
NEW_GEN_MODEL = "1.3 Enter generator model: "
NEW_GEN_MAINTENANCE = "1.4 Change oil period (in hours): "


MAIN_MENU_MAP = {
    1:
        {
            "func": None,
            "sub_menu": [NEW_GEN_NAME, NEW_GEN_DESCR, NEW_GEN_MODEL, NEW_GEN_MAINTENANCE],
        },
    2:
        {
            "func": print_gen_list,
            "sub_menu": []
        },
    3:
        {
            "func": start_gen_work,
            "sub_menu": []
        },
    4:
        {
            "func": stop_gen_work,
            "sub_menu": []
        },
    5:
        {
            "func": None,
            "sub_menu": []
        },
}
