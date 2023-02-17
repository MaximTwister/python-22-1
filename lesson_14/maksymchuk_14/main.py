from abc import ABC, abstractmethod
import json
from ruamel.yaml import YAML
import inspect

class ConfigParser(ABC):

    def __init__(self, config_path):
        self.config_path = config_path
        self.__config_dict: dict = self.parse()

    def __getattr__(self, item):
        value = self.__config_dict.get(item)
        if not value:
            print(f"error: no such config field: `{item}` available")
        return value

    def __getattribute__(self, item: str):
        caller = inspect.stack()[1].function
        print(f"inspect stack: {caller}")
        print(f"__getattribute__ for item: {item}")

        if item.count("__") and caller != "__getattr__":
            print("error: class not providing access to private attributes")
            return None
        return super().__getattribute__(item)

    @property
    def fields(self):
        return list(self.__config_dict.keys())

    def read_cfg(self):
        with open(file=self.config_path) as cfg:
            return cfg.read()

    @abstractmethod
    def parse(self) -> dict:
        pass


class JSONConfigParser(ConfigParser):
    def __init__(self, config_path):
        super().__init__(config_path=config_path)

    def parse(self) -> dict:
        raw_data = self.read_cfg()
        data = json.loads(raw_data)
        print(f"Parsed JSON data: {data}")
        return data


class YAMLConfigParser(ConfigParser):
    def __init__(self, config_path):
        super().__init__(config_path=config_path)

    def parse(self) -> dict:
        raw_data = self.read_cfg()
        yaml = YAML(typ="safe")
        data = yaml.load(raw_data)
        print(f"Parsed YAML data: {data}")
        return data


class XMLConfigParser(ConfigParser):
    def __init__(self, config_path):
        super().__init__(config_path=config_path)

    def parse(self) -> dict:
        return 23


json_cfg = JSONConfigParser(config_path="./json_config.json")
print(json_cfg.fields)
print(json_cfg.host)
print(json_cfg.name)
print(json_cfg._ConfigParser__config_dict)

yaml_cfg = YAMLConfigParser(config_path="./yaml_config.yaml")
xml_cfg = XMLConfigParser(config_path="./yaml_config.yaml")
