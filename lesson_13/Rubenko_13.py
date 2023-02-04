import configparser
import io
import requests
import threading
import time

from PIL import Image

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

path_to_files_download = "C:\My_Python_test_projects\myWD\Lesson_13_OOP_start\\folder"

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
        self.section_api_data = {}
        for el in config.sections():
            search_images_url = config.get(el, "Endpoint")
            key = config.get(el, "Key")
            per_page = config.get(el, "FilesAmount")
            image_type = config.get(el, "imageType")
            q = config.get(el, "Theme")
            self.section_api_data[el] = {"url": search_images_url,
                                         "q": q,
                                         "key": key,
                                         "image_type": image_type,
                                         "per_page": per_page}
            print(self.section_api_data)

    @staticmethod
    def calc_action_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func_to_wrap = func(*args, **kwargs)
            end = time.time()
            action_time = end - start
            print(f" action time of func <{func.__name__}> = {action_time} sec")
            return func_to_wrap
        return wrapper

    @calc_action_time
    def sync_download(self):
        images_urls_list, images_files_names_list = [], []
        for el in self.section_api_data.values():
            image_request_res = requests.get(url=el["url"], params={"q": el['q'],
                                                                    "key": el['key'],
                                                                    'image_type': el['image_type'],
                                                                    "per_page": el['per_page']})

            response_res = image_request_res.json().get("hits")
            images_urls_list.extend([response_res[el].get("largeImageURL") for el in range(0, len(response_res) - 1)])
            images_files_names_list.extend([images_urls_list[el].split('/')[-1] for el in range(0, len(images_urls_list) - 1)])
        path = path_to_files_download
        for el in range(0, len(images_urls_list) - 1):
            url = images_urls_list[el]
            file_name = images_files_names_list[el]
            res = requests.get(url)
            image = Image.open(io.BytesIO(res.content))
            image.save(f"{path}/{file_name}")

    @calc_action_time
    def async_download(self):
        threads = []
        for i in range(10):
            threads.append(threading.Thread(target=self.sync_download))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def get_theme(self):
        print()
        for el in self.section_api_data:
            print(f" Theme -> {self.section_api_data[el]['q']}")


def main():
    i = ImagesDownloader("websites_api_data.ini")
    i.sync_download()
    i.async_download()
    i.get_theme()


main()

