import os
from unittest.mock import Mock, patch

import testing.postgresql
from sqlalchemy import create_engine
import psycopg2
import pytest

from pluto._internal.adapters.storemgr import PGSQLStorageManager
from pluto._internal.config.config import Config

@pytest.fixture
def basic_envvars():
    os.environ["HOST"] = "localhost"
    os.environ["PORT"] = "8999"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_USER"] = "pluto_dog"
    os.environ["DB_PASSWORD"] = "you-shall-not-pass"
    os.environ["DB_PORT"] = "1234"
    os.environ["DB_NAME"] = "pluto"

@pytest.fixture
def empty_envvars():
    for k in os.environ:
        os.environ.pop(k)

@pytest.fixture
def basic_config(basic_envvars):
    return Config.parse()

@pytest.fixture
def mock_dbconnect():
    class CursorCol:
        def __init__(self, name):
            self.name = name
    def cursor_cols(names):
        cols = []
        for name in names:
            cols.append(CursorCol(name))
        return cols

    with patch("psycopg2.connect") as mock_connect:
        def mock_func(expected_query, expected_cols, expected_rows):
            mock_cursor = Mock()
            mock_cursor.fetchall.return_value = expected_rows
            mock_cursor.rowcount = len(expected_rows)
            mock_cursor.description = cursor_cols(expected_cols)
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
def real_storemgr(basic_config, setup_real_pg):
    storemgr = PGSQLStorageManager(basic_config)
    storemgr._conn = psycopg2.connect(**setup_real_pg.dsn())
    yield storemgr

@pytest.fixture
def real_storemgr_configured(
        real_storemgr,
        putin_user,
        bj_user,
        users_table,
        income_table,
        expense_table,
        expense_tag_table,
):
    # Create default tables
    real_storemgr.create_table("users", users_table)
    real_storemgr.create_table("income", income_table)
    real_storemgr.create_table("expense", expense_table)
    real_storemgr.create_table("expense_tag", expense_tag_table)

    # Add some default users to facilitate testing
    real_storemgr.insert("users", putin_user)
    real_storemgr.insert("users", bj_user)

    yield real_storemgr

@pytest.fixture
def users_table():
    return dict(
        id="char(32)",
        name="char(32)",
        email="char(64)",
        password="char(32)",
    )

@pytest.fixture
def income_table():
    return dict(
        id="char(32)",
        user_id="char(32)",
        src="char(32)",
        amount="real",
        inc_date="date",
    )

@pytest.fixture
def expense_table():
    return dict(
        id="char(32)",
        user_id="char(32)",
        src="char(32)",
        amount="real",
        exp_date="date",
    )

@pytest.fixture
def expense_tag_table():
    return dict(
        expense_id="char(32)",
        tag_name="char(32)",
    )

@pytest.fixture
def putin_user():
    return dict(
        id="putin",
        name="vladimir putin",
        email="putin@russia.ru",
        password="123"
    )

@pytest.fixture
def bj_user():
    return dict(
        id="bj",
        name="b j",
        email="bj@b.j",
        password="321",
    )
