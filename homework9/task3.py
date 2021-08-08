"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.

If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6

"""
from os import listdir
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    list_of_files = listdir(dir_path)
    count = 0
    for file in list_of_files:
        if not file.endswith(file_extension):
            continue

        with open(f"{dir_path}/{file}") as file_to_count:
            for line in file_to_count:
                if tokenizer:
                    count += len(tokenizer.__call__(line))
                else:
                    count += 1
    return count
