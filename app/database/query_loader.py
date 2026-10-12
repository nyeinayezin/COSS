from functools import lru_cache
from pathlib import Path
import re


SQL_DIR = Path(__file__).resolve().parent / "sql"


@lru_cache(maxsize=None)
def load_queries(filename):
    sql_file = SQL_DIR / filename
    content = sql_file.read_text(encoding="utf-8")

    markers = list(
        re.finditer(
            r"(?m)^-- name:\s*(\w+)\s*$",
            content
        )
    )

    if not markers:
        raise ValueError(
            f"No named queries found in {filename}"
        )

    queries = {}

    for index, marker in enumerate(markers):
        start = marker.end()

        if index + 1 < len(markers):
            end = markers[index + 1].start()
        else:
            end = len(content)

        name = marker.group(1)
        sql = content[start:end].strip()

        if not sql:
            raise ValueError(
                f"Query '{name}' is empty in {filename}"
            )

        if name in queries:
            raise ValueError(
                f"Duplicate query name '{name}' in {filename}"
            )

        queries[name] = sql

    return queries