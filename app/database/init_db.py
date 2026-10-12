
import sqlite3

from config import DATABASE_PATH, SCHEMA_PATH


def initialise_database():
    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(schema_sql)

    print(f"Database created successfully: {DATABASE_PATH}")


if __name__ == "__main__":
    initialise_database()