#!/usr/bin/python3
"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0

    def recursive_search(tree, element):
        nonlocal counter
        tree = list(tree.values()) if isinstance(tree, dict) else list(tree)
        for item in tree:
            if isinstance(item, str):
                if item == element:
                    counter += 1
            else:
                recursive_search(item, element)
        return counter

    return recursive_search(tree, element)


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
