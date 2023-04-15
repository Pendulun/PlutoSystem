from unittest import mock

import psycopg2
import pytest


from pluto._internal.adapters.storemgr import StorageManager

class TestStorageManager:
    @pytest.fixture
    def storemgr(self, basic_config):
        return StorageManager(basic_config)

    def test_init(self, storemgr):
        pass

    def test_insert(self, storemgr, mock_dbconnect):
        ass = mock_dbconnect(
            expected_query=("INSERT INTO users (id, first_name, last_name) "+
                            "VALUES ('bg', 'billy', 'graham')"),
            expected_rows=[],
        )
        storemgr.connect()
        storemgr.insert("users", dict(id='bg', first_name='billy',
                                      last_name='graham'))
        storemgr.close_conn()
        ass()

    def test_select_star(self, storemgr, mock_dbconnect):
        expected_query = "SELECT * FROM users"
        expected_rows = [('bg', 'billy', 'graham')]
        ass = mock_dbconnect(
            expected_query=expected_query,
            expected_rows=expected_rows,
        )
        storemgr.connect()
        res = storemgr.select_star("users")
        storemgr.close_conn()
        ass()
        assert res == expected_rows
