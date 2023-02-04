import requests

from constentes import BASE_URL_PIXABAY  # type: ignore


def get_list_image(params):
    data, err = None, None

    try:
        response = requests.get(BASE_URL_PIXABAY, params=params)
        data_images = response.json()["hits"]
        data = data_images
        return data, err
    except requests.exceptions.HTTPError:
        err = "Server request respond with an error"
        return data, err
