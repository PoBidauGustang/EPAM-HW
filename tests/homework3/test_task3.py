import pytest

from homework3.task3 import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_task():
    assert make_filter(name="polly", type="bird").apply(sample_data) == [sample_data[1]]


def test_filter_even():
    evan = Filter(lambda a: isinstance(a, int), lambda a: a % 2 == 0)
    assert evan.apply(range(9)) == [0, 2, 4, 6, 8]


def test_no_match():
    assert make_filter(type="person", name="name").apply(sample_data) == []


def test_no_common_filters():
    assert make_filter(occupation="was here", type="person").apply(sample_data) == [
        sample_data[0]
    ]


def test_no_filter():
    assert make_filter().apply(sample_data) == sample_data
