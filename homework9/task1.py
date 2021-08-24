"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    with open(file_list[0]) as file1, open(file_list[1]) as file2:
        content = []
        for i, z in zip(file1, file2):
            content.append(int(i.strip()))
            content.append(int(z.strip()))
    return iter(content)
