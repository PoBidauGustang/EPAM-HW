import pytest

from homework2.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    assert get_longest_diverse_words("tests/homework2/data.txt") == [
        "vorgebahnte",
        "Betrachtung",
        "ausführen",
        "verbirgt",
        "vielmehr",
        "bedenkli",
        "Waldgang",
        "Ausflug",
        "hinter",
        "gefaßt",
    ]


def test_get_rarest_char():
    assert get_rarest_char("tests/homework2/data.txt") == "S"


def test_count_punctuation_chars():
    assert count_punctuation_chars("tests/homework2/data.txt") == 5


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("tests/homework2/data.txt") == 11


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("tests/homework2/data.txt") == "ü"
