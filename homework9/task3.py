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
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    files = Path(dir_path).glob(f"*.{file_extension}")
    count = 0
    for file in files:
        with open(f"{file}") as file_to_count:
            for line in file_to_count:
                if tokenizer:
                    count += len(tokenizer.__call__(line))
                else:
                    count += 1
    return count
