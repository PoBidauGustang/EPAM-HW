import requests
from requests.exceptions import RequestException


def count_dots_on_i(url: str) -> int:
    try:
        data = requests.get(url).content
    except RequestException:
        raise ValueError(f"Unreachable {url}")
    return str(data).count("i")
