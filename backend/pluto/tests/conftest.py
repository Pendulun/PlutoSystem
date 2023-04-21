import os
from unittest.mock import Mock, patch

import testing.postgresql
from sqlalchemy import create_engine
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

# setup_real_pg sets up a PG instance in a temp dir for integration testing.
@pytest.fixture
def setup_real_pg():
    with testing.postgresql.Postgresql() as postgresql:
        create_engine(postgresql.url())
        print(postgresql.url())
        print(postgresql.dsn())
        yield postgresql

@pytest.fixture
def putin_user():
    return dict(
        id="putin",
        first_name="vladimir",
        last_name="putin",
    )

@pytest.fixture
def bj_user():
    return dict(
        id="bj",
        first_name="b",
        last_name="j",
    )
