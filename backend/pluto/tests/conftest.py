import os
from unittest.mock import Mock, patch

import psycopg2
import pytest

from pluto._internal.config.config import Config

@pytest.fixture
def basic_envvars():
    os.environ["HOST"] = "localhost"
    os.environ["PORT"] = "8999"
    os.environ["DBHOST"] = "localhost"
    os.environ["DBUSER"] = "pluto_dog"
    os.environ["DBPASSWORD"] = "you-shall-not-pass"
    os.environ["DBPORT"] = "1234"
    os.environ["DBNAME"] = "pluto"

@pytest.fixture
def empty_envvars():
    for k in os.environ:
        os.environ.pop(k)

@pytest.fixture
def basic_config(basic_envvars):
    return Config.parse()

@pytest.fixture
def mock_dbconnect():
    # class Connection:

    #     def __init__(self, expected_query: str, expected_rows: list[list[str]]):
    #         self.expected_query = expected_query
    #         self.expected_rows = expected_rows

    #     class Cursor:
    #         def __init__(self, conn):
    #             self._conn = conn

    #         def execute(self, query: str):
    #             if query == self._conn.expected_query:
    #                 return
    #             raise ValueError(f"Cursor received unexpected query {query}")

    #         def fetchall(self) -> list[list[str]]:
    #             return self._conn.expected_rows

    #     def cursor(self):
    #         return Cursor(self)

    #     def commit(self):
    #         pass
    # return lambda query, expected_rows: Connection(query, expected_rows)

    with patch("psycopg2.connect") as mock_connect:
        def mock_func(expected_query, expected_rows):
            mock_cursor = Mock()
            mock_cursor.fetchall.return_value = expected_rows
            mock_cursor.rowcount = len(expected_rows)
            mock_conn = Mock()
            mock_conn.cursor.return_value = mock_cursor
            mock_connect.return_value = mock_conn

            # Assert that the mock objects were called correctly
            def mock_assert():
                mock_connect.assert_called_once()
                mock_conn.cursor.assert_called_once()
                mock_cursor.execute.assert_called_once_with(expected_query)

                if expected_query.startswith("SELECT") and len(expected_rows) > 0:
                    mock_cursor.fetchall.assert_called_once()

            return mock_assert

        yield mock_func
