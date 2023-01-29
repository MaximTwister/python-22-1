import json
import requests
import os
from Pillow import Image
from datetime import datetime
from threading import Thread as th

# from constants import PER_PAGE

PER_PAGE = 50

api_key = os.environ["PIXABAY_API_KEY"]


def timer(func):
    print("timer decorator")


def wrapper(*args, **kwargs):
    print(f"[wrapper] start function: {func.__name__}")
    start = datetime.now()
    func(*args, **kwargs)
    total = datetime.now() - start
    print(f"[wrapper]function: {func.__name__} takes {total}")
    return wrapper()


def dialog():
    print("What topic would you like to see the photo?\nThis value may not exceed 100 characters.\n"
          "Example: yellow + flower\n")
    topic = input("->").lower()
    return topic


@ def synchronous_downloads():
    topic = dialog()
    url = f'https://pixabay.com/api/?key={api_key}&q={topic}'
    response = requests.get(url=url)
    data = json.loads(response.content)
    url_images = [it["pageURL"] for it in data['hits']]

    for ind in range(PER_PAGE):
        res = requests.get(url=url_images[ind])
        print({res.headers["Content-Type"]})
        print(type(res))

        if response.headers['Content-Type'] == "jpeg":
            with Image.open(f"{num}.jpeg", 'wb') as image_file:
                image_file.write(response.content)


@ def separate_threads_downloads():
    topic = dialog()
    url = f'https://pixabay.com/api/?key={api_key}&q={topic}'
    response = requests.get(url=url)
    data = json.loads(response.content)
    url_images = [it["pageURL"] for it in data['hits']]

    for ind in range(PER_PAGE):
        res = requests.get(url=url_images[ind])
        print({res.headers["Content-Type"]})
        print(type(res))

        if response.headers['Content-Type'] == "jpeg":
            with Image.open(f"{num}.jpeg", 'wb') as image_file:
                image_file.write(response.content)

    t = th(target=separate_threads_downloads, args=1, ))
    t.start()


def main():
    wrapper()


main()




