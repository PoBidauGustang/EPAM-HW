import sqlite3


def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    dictionary = {}
    for index, col in enumerate(cursor.description):
        dictionary[col[0]] = row[index]
    return dictionary


class TableData:
    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.database_name)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def __len__(self) -> int:
        self.cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return self.cursor.fetchone()["COUNT(*)"]

    def __getitem__(self, item: str) -> tuple:
        self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:item", {"item": item}
        )
        return self.cursor.fetchone()

    def __contains__(self, item: str) -> bool:
        self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:item", {"item": item}
        )
        return self.cursor.fetchone()

    def __iter__(self):
        yield from self.cursor.execute(f"SELECT * from {self.table_name}")
