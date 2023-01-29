import requests
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


from common import (
    url,
    params,
)
from utils import (
    download_image,
    timeit,
    prepare_images_path,
    sort_hits_by_img_size,
)


@timeit
def sync_download(hits: list):
    for hit in hits:
        download_image(hit)


@timeit
def async_download_origin(hits: list):
    threads = []
    for hit in hits:
        threads.append(Thread(target=download_image, args=(hit,)))
    [th.start() for th in threads]
    [th.join() for th in threads]


@timeit
def async_download_tpe(hits: list):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for hit in hits:
            executor.submit(download_image, hit_obj=hit)


def main():
    res = requests.get(url=url, params=params)
    hits: list = res.json()["hits"]
    print(sort_hits_by_img_size(hits))
    downloaders = {
        # "synchronous": sync_download,
        "asynchronous origin": async_download_origin,
        "asynchronous TPE": async_download_tpe,
    }
    # for download_type, downloader in downloaders.items():
    #     print(f"\n=== {download_type} download starts===")
    #     prepare_images_path()
    #     downloader(hits)


main()
