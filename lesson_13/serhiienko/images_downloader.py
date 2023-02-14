import shutil
import requests
import io
import os
from configparser import ConfigParser
from PIL import Image
from concurrent.futures import ThreadPoolExecutor


class ImagesDownloader:
    """
    This class takes path to config files
    Config file example:
        [pixabay.com]
        Endpoint = https://pixabay.com/api/
        Key = 33189387-d9991af6fab6f6c7b9e4ceb7a
        Files Amount = 5
        Theme = space
        Directory Image = images
    """

    def __init__(self, path: str):
        self.path: str = path
        self.path_directory_images: str = ""
        self.params: dict = {}
        self.endpoint: str = ""
        self.hits: dict = []

        self.__parse_config()
        self.get_list_images()

    def __parse_config(self):
        """
        This is a private class method that parses the config file
        """

        config = ConfigParser()
        config.read(self.path)

        self.endpoint: str = config["pixabay.com"]["endpoint"]

        self.path_directory_images: str = config["pixabay.com"]["Directory Image"]

        self.params["key"]: str = config["pixabay.com"]["key"]
        self.params["per_page"]: int = config["pixabay.com"]["Files Amount"]
        self.params["q"]: str = config["pixabay.com"]["Theme"]
        self.params["image_type"]: str = config["pixabay.com"]["Theme"]

    def set_directory_path(self, path: str):
        """
        This method accepts a path to a directory where your images will be saved.
        :param path: <str>
        :return: None
        """

        self.path_directory_images: str = path

    def get_params(self):
        """
        This method return currency params from instance class
        :return: params
        """

        return self.params

    def set_theme(self, theme: str):
        """
        The method sets the theme for receiving images.
        :param theme: <str>
        :return: None
        """

        self.params["q"]: str = theme

    def download_image(self, hit_obj: dict):
        """
        This method downloads the image and saves it to the current directory set in the class
        :param hit_obj: {
            "largeImageURL": "<str>"
            "id": "<int>"
        }
        :return: None
        """

        hit_url: str = hit_obj.get("largeImageURL")
        hit_id: int = hit_obj.get("id")

        res = requests.get(url=hit_url)

        _, file_extension = os.path.splitext(hit_url)
        im = Image.open(io.BytesIO(res.content))
        im.save(f"{self.path_directory_images}/{hit_id}{file_extension}")

    def sync_download(self):
        """
        Downloads all images stored in the class in the hits field synchronously
        :return: None
        """

        for hit in self.hits:
            self.download_image(hit)

    def async_download(self, max_workers=10):
        """
        Downloads all images stored in the class in the hits field asynchronously
        :param max_workers: <int>
        :return: None
        """

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for hit in self.hits:
                executor.submit(self.download_image, hit_obj=hit)

    def prepare_images_path(self):
        """
        This method creates the directory if it doesn't exist. If the directory exists, it removes all content.
        :return: None
        """
        if os.path.exists(self.path_directory_images):
            shutil.rmtree(self.path_directory_images)
        os.mkdir(self.path_directory_images)

    def get_list_images(self):
        """
        This method makes a request with parameters for images and stores them in a field of the hits class
        :return: None
        """
        res = requests.get(url=self.endpoint, params=self.params)
        self.hits = res.json()["hits"]
