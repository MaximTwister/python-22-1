from functools import wraps
from PIL import Image

import io
import requests
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def download_image(url, file_name):
    res = requests.get(url)
    im = Image.open(io.BytesIO(res.content))
    im.save(f"images/{file_name}.jpg")
