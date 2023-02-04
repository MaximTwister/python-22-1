import io
import os
import requests
import threading
import time

from PIL import Image


api_key = os.environ["PIXABAY_API_KEY"]
search_images_api = "https://pixabay.com/api"
path_synchronous_saving = "C:\My_Python_test_projects\myWD\Lesson_12\synchronous\\"
path_multithreading_saving = "C:\My_Python_test_projects\myWD\Lesson_12\multithreading\\"


def get_user_images_request():
    err = None
    while True:
        try:
            user_request = input(str("Please enter your search term to upload images. For example <kitten> or <puppy> : "))
            break
        except TypeError as err:
            print(f"{err} - Invalid input type")
            return None
    return user_request


def calc_action_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_to_wrap = func(*args, **kwargs)
        end = time.time()
        action_time = end - start
        print(f" action time of func <{func.__name__}> = {action_time} sec")
        return func_to_wrap
    return wrapper


def get_images_urls(params):
    image_request_res = requests.get(url=search_images_api, params=params)
    response_res = image_request_res.json().get("hits")
    images_urls_list = [response_res[el].get("largeImageURL") for el in range(0, len(response_res)-1)]
    return images_urls_list


def get_images_files_names(urls: list) -> list | None:
    images_files_names = [urls[el].split('/')[-1] for el in range(0, len(urls)-1)]
    return images_files_names


@calc_action_time
def synchronous_files_downloads(urls: list, files_names: list, path=path_synchronous_saving):
    for el in range(0, len(urls)-1):
        url = urls[el]
        file_name = files_names[el]
        res = requests.get(url)
        image = Image.open(io.BytesIO(res.content))
        image.save(f"{path}/{file_name}")


@calc_action_time
def multithreading_files_downloads(urls: list, files_names: list, path=path_multithreading_saving):
    threads = []
    #for i in range(len(list)):
    for i in range(50):
        threads.append(threading.Thread(target=synchronous_files_downloads, args=(urls, files_names, path)))
    for thread in threads:
        thread.start()


def main():
    user_image_object = get_user_images_request()
    api_params = {"q": user_image_object, 'key': api_key, "image_type": "photo", "per_page": 50}
    all_files_urls = get_images_urls(api_params)
    all_files_names = get_images_files_names(all_files_urls)
    synchronous_files_downloads(all_files_urls, all_files_names,)
    multithreading_files_downloads(all_files_urls, all_files_names,)


main()



