import configparser
import ruamel.yaml
import json

class ConfigParser:
    def __init__(self, path):
        self.config_path = path

    def parse_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        data = {}
        for section in config.sections():
            data[section] = {}
            for name, value in config.items(section):
                data[section].update({name: value})
        return data


class YamlConfigParser(ConfigParser):
    def yaml_parser(self):
        yaml = ruamel.yaml.YAML(typ='unsafe')
        some_config_pars = self.parse_config()
        print(some_config_pars)
        with open("test_yaml_config.yaml", "w") as f:
            yaml.dump(some_config_pars, f)


class JsonParser(ConfigParser):
    def json_parser(self):
        some_config_pars = self.parse_config()
        print(some_config_pars)
        with open("test_yaml_config.json", "w") as f:
            json.dump(some_config_pars, f)

def main():
    obj_to_convert_yml = YamlConfigParser("C:\My_Python_test_projects\myWD\Lesson_14\HW\websites_api_data.ini")
    obj_to_convert_yml.yaml_parser()
    obj_to_convert_json = JsonParser("C:\My_Python_test_projects\myWD\Lesson_14\HW\websites_api_data.ini")
    obj_to_convert_json.json_parser()

main()
