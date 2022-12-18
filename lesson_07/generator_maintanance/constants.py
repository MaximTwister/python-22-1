GEN_KEYS = ["name", "description", "model", "change_oil_period"]
TABLE_TITLES = ["id", "name", "description", "model", "motohours", "state", "oil"]
GEN_DB_FILE = "./gen_db"

# Generators states:
STOPPED = 0
WORKING = 1

# Menu options
MAIN_MENU_OPTION = 0
LIST_GEN_MENU_OPTION = 2

GOOD = "✅"
MAINTENANCE = "⚠️"

EMPTY_SESSION = {"start": None, "stop": None}
