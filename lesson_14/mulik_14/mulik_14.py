import json
from ruamel.yaml import YAML


class ConfigParser:
    def __init__(self):
        self.data = self.parse_config()

    def parse_config(self):
        return {}

    def fruits(self):
        return self.data["fruits"]


class YAMLParser(ConfigParser):
    def parse_config(self):
        with open("sasha.yaml", "rt") as f:
            yaml = YAML(typ='safe')  # default, if not specfied, is 'rt' (round-trip)
            return yaml.load(f.read())


class JSONParser(ConfigParser):
    def parse_config(self):
        with open("sasha.json", "rt") as f:
            return json.loads(f.read())
