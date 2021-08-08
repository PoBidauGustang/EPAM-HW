from pathlib import Path

from homework9.task3 import universal_file_counter

test_dir = Path("./tests/homework9/")


def test_from_example_1():
    assert universal_file_counter(test_dir, "txt") == 6


def test_from_example_2():
    assert universal_file_counter(test_dir, "txt", str.split) == 6


tests_sub_folder = Path("./tests/homework9/tests_sub_folder")


def test_count_lines():
    assert universal_file_counter(tests_sub_folder, "txt") == 8


def test_count_words():
    assert universal_file_counter(tests_sub_folder, "txt", str.split) == 23
