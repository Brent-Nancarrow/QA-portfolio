import json
import sqlite3
from pathlib import Path


def create_database_from_sql(db_path: Path, schema_path: Path, seed_path: Path) -> sqlite3.Connection:
    """
    Create a SQLite database from a schema SQL file and a seed-data SQL file.
    Returns an open database connection.
    """
    connection = sqlite3.connect(db_path)

    with open(schema_path, "r", encoding="utf-8") as schema_file:
        connection.executescript(schema_file.read())

    with open(seed_path, "r", encoding="utf-8") as seed_file:
        connection.executescript(seed_file.read())

    connection.commit()
    return connection


def fetch_one_value(connection: sqlite3.Connection, query: str):
    """
    Run a SQL query and return the first value from the first row.
    Good for totals, counts and sums.
    """
    cursor = connection.execute(query)
    row = cursor.fetchone()
    return row[0] if row else None


def fetch_all_rows(connection: sqlite3.Connection, query: str):
    """
    Run a SQL query and return all rows.
    Useful for more detailed checks.
    """
    cursor = connection.execute(query)
    return cursor.fetchall()


def load_expected_dashboard_values(json_path: Path) -> dict:
    """
    Load the expected dashboard/report values from a JSON file.
    """
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)