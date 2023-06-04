from typing import List

import requests

from settings import COLLECTOR_URL_WITH_API_PREFIX


request_methods_mapper = {"post": requests.post, "get": requests.get}


def get_url(endpoint):
    return f"{COLLECTOR_URL_WITH_API_PREFIX}/{endpoint}/"


def send_data(url: str, data: List[dict], http_method="post"):
    request_method = request_methods_mapper.get(http_method)
    print(f"method: {request_method}, data: {data}")
    res = request_method(url=url, json=data)
    return res
