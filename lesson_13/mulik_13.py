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
import configparser
import io
import requests
import os
from threading import Thread as th
from PIL import Image
import time


class ImagesDownloader:
    """
    This class takes path to config files
    Config file example:
    """

    def __init__(self, path):
        self.config_path = path
        self.params = {}
        self.parse_config(path)

    def parse_config(self, path):
        config = configparser.ConfigParser()
        config.read(path)
        self.sections = {}
        for el in config.sections():
            photo_url = config[el]["Endpoint"]
            key = config[el]["Key"]
            per_page = config[el]["FilesAmount"]
            q = config[el]["Theme"]
            self.sections[el] = {"key": key, "q": q, "per_page": per_page, "photo_url": photo_url}

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

    @staticmethod
    def download_img(img_url, folder=None):
        img = requests.get(url=img_url)
        data = io.BytesIO(img.content)
        image = Image.open(data).convert("RGB")
        data.close()
        image.save(fp=f'{folder}/{img_url.split("/")[-1]}')

    def async_download(self):
        """
        Docstring for `async_download`
        :return:
        """
        for el in self.sections.values():
            res = requests.get(url=el["photo_url"], params={"key": el['key'], "q": el["q"], "per_page": el["per_page"]}).json()
            large_urls = []
            for el in res["hits"]:
                large_url = el["largeImageURL"]
                large_urls.append(large_url)
            for url in large_urls:
                t = th(target=self.download_img, args=(url, 'D:\photo_py_2'))
                t.run()

    def list_sources(self):
        return list(self.sections.keys())

    def get_source(self, name):
        return self.sections[name]


i = ImagesDownloader(path="mulik_13")
i.async_download()
print(i.list_sources())
# 344: pixabay.com
# 377: another-cool-source.com
print(i.get_source(name="pixabay.com"))
# i.set_source(id=377)
# i.set_source(id=344)
# i.get_theme()
# i.set_theme("Cars")
