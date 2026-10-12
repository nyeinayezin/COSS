
import sqlite3

from config import DATABASE_PATH, DATABASE_TIMEOUT


def get_connection():
    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(
        str(DATABASE_PATH),
        timeout=DATABASE_TIMEOUT
    )

    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")

    return connection