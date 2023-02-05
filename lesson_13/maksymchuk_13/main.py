import configparser
import hashlib
from random import randint
from io import BytesIO

import requests
from PIL import Image


class ImagesDownloader:

    fields = {"url", "key", "theme", "path"}
    param_prefix = "param__"

    def __init__(self, config_path):
        self.config_path = config_path
        self.config_hash = None
        self.configs: configparser.ConfigParser = None
        self.default_cfg: configparser.SectionProxy = None
        self.config_type = self.get_config_type()
        self.parce_config()

    def parce_config(self):
        cfg = configparser.ConfigParser()
        cfg.read(self.config_path)
        if not self.is_config_valid(cfg):
            raise ValueError
        self.configs = cfg
        self.default_cfg = cfg[cfg.sections()[0]]
        self.config_hash = self.get_config_hash()

    def is_config_valid(self, cfg: configparser.ConfigParser) -> bool:
        validation_results: list[bool] = []

        if len(cfg.sections()) == 0:
            return False

        for cfg_title in cfg.sections():
            cfg_fields = set(cfg[cfg_title].keys())
            is_all_fields_present = self.fields.issubset(cfg_fields)
            validation_results.append(is_all_fields_present)

        return all(validation_results)

    def get_config_hash(self):
        with open(self.config_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def download_image(self, url: str):
        img_id = randint(1000, 999999)
        res = requests.get(url=url)
        img_object = Image.open(BytesIO(res.content))
        img_name = f"{self.default_cfg['path']}/{self.default_cfg['theme']}_{img_id}.jpg"
        img_object.save(fp=img_name)
        print(f"image {img_name} was saved")

    def sync_download(self):
        res = requests.get(
            url=self.default_cfg["url"],
            params=self.parce_params(),
        )
        # TODO: PIXABAY ONLY
        hits: list = res.json()["hits"]
        images_amount = self.default_cfg.getint("files") # 10
        for idx in range(images_amount):
            try:
                # TODO: PIXABAY ONLY
                self.download_image(hits[idx].get('largeImageURL'))
            except IndexError:
                print(f"warning: impossible to download: {images_amount}"
                      f"got: {len(hits)}")
                break

    def parce_params(self):
        c = self.default_cfg
        return {k.replace(self.param_prefix, ""):v for k, v in c.items() if k.startswith(self.param_prefix)}

    def get_config_type(self):
        if self.config_path.endswith(".cfg"):
            return "general"


d = ImagesDownloader(config_path="./config.cfg")

# Thread to track config changes and reparse config - pitfalls:
# 1. User is still in process of changing config.
# 2. Period to check (?) (probably once per 10 sec).
