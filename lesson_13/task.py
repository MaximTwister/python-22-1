# Download Images Class
# Class takes one parameter path to config file
#
# https://docs.python.org/3/library/configparser.html
# Inside config file:
# [pixabay.com]
# Endpoint = pixabay.com/api
# Key =
# Files Amount =
# Theme = space
# [another-cool-source.com]
#

class ImagesDownloader:
    """
    This class takes path to config files
    Config file example:
    """

    def __init__(self, path):
        self.config_path = path
        self.params = {}
        self.parse_config()

    def parse_config(self):
        pass

    def set_theme(self, theme: str):
        self.params["theme"] = theme

    def sync_download(self, images_amount=1):
        """
        Docstring for `sync_download`
        param: int
            Super cool param
        :return:
        """
        pass

    def async_download(self, images_amount=1):
        """
        Docstring for `async_download`
        :return:
        """
        pass


i = ImagesDownloader(path="test.conf")
# i.async_download(images_amount=10)
# i.list_sources()
# 344: pixabay.com
# 377: another-cool-source.com
# i.get_source()
# i.set_source(id=377)
# i.set_source(id=344)
# i.get_theme()
# i.set_theme("Cars")
