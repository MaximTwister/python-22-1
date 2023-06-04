from dotenv import dotenv_values

config = dotenv_values(".env")

COLLECTOR_HOST = config.get("COLLECTOR_HOST")
COLLECTOR_PORT = config.get("COLLECTOR_PORT")
COLLECTOR_API_PREFIX = config.get("COLLECTOR_API_PREFIX")

# http://127.0.0.1:8000
COLLECTOR_URL = f"http://{COLLECTOR_HOST}:{COLLECTOR_PORT}"
# http://127.0.0.1:8000/collector/api/v1
COLLECTOR_URL_WITH_API_PREFIX = f"{COLLECTOR_URL}/{COLLECTOR_API_PREFIX}"
