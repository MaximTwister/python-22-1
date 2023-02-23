GEN_KEYS = ["name", "description", "model", "change_oil_period"]
TABLE_TITLES = ["id", "name", "description", "model", "total_motohours", "motohours_after_maint", "state", "oil"]
GEN_DB_FILE = "./gen_db"

# Generators states:
STOPPED = 0
WORKING = 1

# Menu options
MAIN_MENU_OPTION = 0
LIST_GEN_MENU_OPTION = 2

GOOD = "All Ok"
MAINTENANCE = "Need maintenance"


EMPTY_SESSION = {"start": None, "stop": None}
EMPTY_SESSION_AFTER_MAINT = {"start": None, "stop": None}