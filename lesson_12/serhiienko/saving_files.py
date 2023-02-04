import random
from threading import Thread as th
from utils import (  # type: ignore
    timeit,
    download_image,
)


@timeit
def synchronous(data_images):
    for image in data_images:
        url = image.get("largeImageURL")
        download_image(url, random.random())


@timeit
def asynchronous(data_images):
    threads = []

    for image in data_images:
        url = image.get("largeImageURL")
        args = (url, random.random())
        threads.append(th(target=download_image, args=args))

    [t.start() for t in threads]
    [t.join() for t in threads]


