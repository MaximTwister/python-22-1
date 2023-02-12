import configparser
import os

path = "test.conf"


class ImagesDownloader:
    """
    This class takes path to config files
    """

    def __init__(self):
        self.config_path = path
        self.params = {}
        self.parse_config(path)

    def create_config(self):
        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section("pixabay.com")
        config.set("pixabay.com", "Endpoint", "pixabay.com/api")
        config.set("pixabay.com", "Key", "33034314-7857bef9539e58c695f105fe1")
        config.set("pixabay.com", "Theme", "space")
        config.set("pixabay.com", "Image_Type", "photo")
        config.set("pixabay.com", "Per_Page", "20")

        with open(self.config_path, "w") as config_file:
            config.write(config_file)

    def parse_config(self, path):
        """
        Create, read, update, delete config
        """
        if not os.path.exists(path):
            self.create_config()

        params = configparser.ConfigParser()
        params.read(path)

    # Читаем некоторые значения из конфиг. файла.
        yield{
            params.get("pixabay.com", "endpoint"),
            params.get("pixabay.com", "key"),
            params.get("pixabay.com", "theme"),
            params.get("pixabay.com", "image_type"),
            params.get("pixabay.com", "per_page")
        }
        print(params)

    # Меняем значения из конфиг. файла.

    def change_per_page(self,params):
        params.set("pixabay.com", "per_page", "12")

    # Удаляем значение из конфиг. файла.
    # params.remove_option("pixabay.com", "theme")

    # Вносим изменения в конфиг. файл.
    # with open(path, "w") as config_file:
    #     params.write(config_file)

        self.parse_config()


 # i = ImagesDownloader.parse_config(self="pixabay.com", path="test.conf")

# i = ImagesDownloader(config_path ="test.conf")