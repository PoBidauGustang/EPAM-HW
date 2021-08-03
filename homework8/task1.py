from typing import Any


def possibly_convert_str_to_int(string: str) -> Any:
    try:
        integer = int(string)
        return integer
    except ValueError:
        return string


class KeyValueStorage:
    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file) as file:
            content = [line.strip() for line in file.readlines()]
        kw_storage = {}

        for line in content:
            attr, value = line.split("=")
            value = possibly_convert_str_to_int(value)
            kw_storage[attr] = value
            self.kw_storage_dict = kw_storage

    def __getattr__(self, item: Any) -> Any:
        return self.kw_storage_dict[item]

    def __getitem__(self, item: Any) -> Any:
        if not item.isidentifier():
            raise ValueError("The key must not start with a number")
        return self.kw_storage_dict[item]
