import io
import requests
import os
from threading import Thread as th
from PIL import Image
import time

api_key = os.environ["PIXABAY_API_KEY"]

photo_url = "https://pixabay.com/api/"


def download_img(img_url, folder=None):
    img = requests.get(url=img_url)
    data = io.BytesIO(img.content)
    image = Image.open(data).convert("RGB")
    data.close()
    image.save(fp=f'{folder}/{img_url.split("/")[-1]}')


def synchronous(urls):
    for url in urls:
        download_img(url, 'D:\photo_py')


def separate(urls):
    for url in urls:
        t = th(target=download_img, args=(url, 'D:\photo_py_2'))
        t.run()


q = input("Enter word(s): ")

photo = {"key": api_key, "q": q, "per_page":50}

res = requests.get(url=photo_url, params=photo).json()

large_urls = []
for el in res["hits"]:
    large_url = el["largeImageURL"]
    large_urls.append(large_url)


start_synch = time.time()
synchronous(large_urls)
end_synch = time.time() - start_synch
print(end_synch)

start_separ = time.time()
separate(large_urls)
end_separ = time.time() - start_separ
print(end_separ)
