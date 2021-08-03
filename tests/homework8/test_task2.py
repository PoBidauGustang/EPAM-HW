from homework8.task2 import TableData

presidents = TableData("tests/homework8/example.sqlite", "presidents")
books = TableData("tests/homework8/example.sqlite", "books")


def test_len_function():
    assert len(presidents) == 3
    assert len(books) == 3


def test_getitem_function():
    assert presidents["Yeltsin"] == {"name": "Yeltsin", "age": 999, "country": "Russia"}
    assert books["1984"] == {"name": "1984", "author": "Orwell"}


def test_contains_function_positive():
    assert "Trump" in presidents
    assert "1984" in books


def test_contains_function_negative():
    assert "Putin" not in presidents
    assert "Movie" not in books


def test_iteration_with_presidents(capsys):
    for president in presidents:
        print(president["name"])
    captured = capsys.readouterr()
    assert captured.out == "Yeltsin\nTrump\nBig Man Tyrone\n"


def test_iteration_with_books(capsys):
    for book in books:
        print(book["name"])
    captured = capsys.readouterr()
    assert captured.out == "Farenheit 451\nBrave New World\n1984\n"
