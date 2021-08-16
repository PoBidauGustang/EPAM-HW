import sqlite3
from typing import Generator


def convert_row_from_tuple_to_dict(cursor: sqlite3.Cursor, row: tuple) -> dict:
    dictionary = {}
    for index, col in enumerate(cursor.description):
        dictionary[col[0]] = row[index]
    return dictionary


def create_cursor(func):
    def wrapper(self, *args, **kwargs):
        connection = sqlite3.connect(self.database_name)
        connection.row_factory = convert_row_from_tuple_to_dict
        cursor = connection.cursor()
        try:
            return func(self, cursor, *args, **kwargs)
        finally:
            cursor.close()
            connection.close()

    return wrapper


class TableData:
    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name

    @create_cursor
    def __len__(self, cursor) -> int:
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return cursor.fetchone()["COUNT(*)"]

    @create_cursor
    def __getitem__(self, cursor, item: str) -> tuple:
        cursor.execute(
            f"SELECT * from {self.table_name} where name=:item", {"item": item}
        )
        return cursor.fetchone()

    @create_cursor
    def __contains__(self, cursor, item: str) -> bool:
        cursor.execute(
            f"SELECT * from {self.table_name} where name=:item", {"item": item}
        )
        return cursor.fetchone()

    def __iter__(self) -> Generator:
        self.connection = sqlite3.connect(self.database_name)
        self.connection.row_factory = convert_row_from_tuple_to_dict
        self.cursor = self.connection.cursor()
        yield from self.cursor.execute(f"SELECT * from {self.table_name}")
        self.cursor.close()
        self.connection.close()
