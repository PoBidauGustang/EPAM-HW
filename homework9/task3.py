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
from itertools import chain
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    files = Path(dir_path).glob(f"*.{file_extension}")
    count = 0
    if tokenizer:
        text = (tokenizer(path.read_text()) for path in files)
        count = sum(map(len, text))
    else:
        text = chain.from_iterable(((path.read_text().split("\n")) for path in files))
        count = len(tuple(text))
    return count
