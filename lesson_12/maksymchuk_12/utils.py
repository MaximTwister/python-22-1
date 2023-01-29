import os
import shutil
import time
from io import BytesIO
from pprint import pprint

import requests
from PIL import Image

from common import images_path, images_theme


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        duration = time.time() - start
        print(f"takes {duration} seconds")
    return wrapper


def download_image(hit_obj: dict):
    print(f"hit object to download: {hit_obj}")
    hit_url = hit_obj.get("largeImageURL")
    hit_id = hit_obj.get("id")
    res = requests.get(url=hit_url)
    img_object = Image.open(BytesIO(res.content))
    img_object.save(f"{images_path}/{images_theme}_{hit_id}.jpg")
    print(f"image {images_theme}_{hit_id} was saved")


def prepare_images_path():
    if os.path.exists(images_path):
        shutil.rmtree(images_path)
    os.mkdir(images_path)


def sort_hits_by_img_size(hits: list) -> list:
    sorted_hits = sorted(
        hits,
        reverse=True,
        key=lambda hit: hit.get("imageSize"),
    )
    return sorted_hits
