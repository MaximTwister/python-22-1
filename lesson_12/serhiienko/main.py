import os

from pixabay import get_list_image  # type: ignore
from saving_files import synchronous, asynchronous  # type: ignore


def main():
    key = os.environ("KEY")

    params = {
        "key": key,
        "q": "yellow+flower",
        "per_page": "50"
    }

    data_images, error = get_list_image(params)

    if error:
        print(error)
        return

    asynchronous(data_images)
    synchronous(data_images)


main()
