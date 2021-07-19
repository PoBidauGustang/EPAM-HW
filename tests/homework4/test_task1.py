import os

import pytest

from homework4.task1 import read_magic_number


@pytest.fixture()
def get_file():
    with open("testfile", "w"):
        ...
    yield "testfile"
    os.remove("testfile")


def test_read_magic_number_valid_number(get_file):
    with open(get_file, "w") as testfile:
        testfile.write("2")
    assert read_magic_number(get_file)


def test_read_magic_number_left_border_number(get_file):
    with open(get_file, "w") as testfile:
        testfile.write("1")
    assert read_magic_number(get_file)


def test_read_magic_number_right_border_number(get_file):
    with open(get_file, "w") as testfile:
        testfile.write("2.99999")
    assert read_magic_number(get_file)


def test_read_magic_number_beyond_left_border_negative_number(get_file):
    with open(get_file, "w") as testfile:
        testfile.write("-3")
    assert not read_magic_number(get_file)


def test_read_magic_number_beyond_right_border_number(get_file):
    with open(get_file, "w") as testfile:
        testfile.write("3")
    assert not read_magic_number(get_file)


def test_read_magic_number_not_a_number(get_file):
    with open(get_file, "w") as testfile:
        testfile.write("dgsgrw")
    with pytest.raises(ValueError, match="Something went wrong"):
        read_magic_number(get_file)


def test_read_magic_number_not_a_file_or_directory(get_file):
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        read_magic_number("non-existent file")
