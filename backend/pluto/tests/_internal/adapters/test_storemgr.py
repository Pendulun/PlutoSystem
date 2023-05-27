import psycopg2
import pytest


from pluto._internal.adapters.storemgr import PGSQLStorageManager

class TestStorageManager:
    @pytest.fixture
    def storemgr(self, basic_config):
        return PGSQLStorageManager(basic_config)

    def test_init(self, storemgr):
        pass

    def test_fmtsqlcols(self, storemgr):
        s = storemgr._fmtsqlcols([])
        assert s == "*"
        s = storemgr._fmtsqlcols(["col1"])
        assert s == "col1"
        s = storemgr._fmtsqlcols(["col1", "col2"])
        assert s == "col1, col2"

    def test_insert(self, storemgr, mock_dbconnect):
        ass = mock_dbconnect(
            expected_query=("INSERT INTO users (id, first_name, last_name) "+
                            "VALUES ('bg', 'billy', 'graham')"),
            expected_cols=(),
            expected_rows=[],
        )
        storemgr.connect()
        storemgr.insert("users", dict(id='bg', first_name='billy',
                                      last_name='graham'))
        storemgr.close_conn()
        ass()

    def test_select_star(self, storemgr, mock_dbconnect):
        expected_query = "SELECT * FROM users"
        expected_cols = ('id', 'first_name', 'last_name')
        expected_vals = ('bg', 'billy', 'graham')
        expected_dict = {elem[0]: elem[1] for elem in zip(expected_cols, expected_vals)}
        ass = mock_dbconnect(
            expected_query=expected_query,
            expected_cols=expected_cols,
            expected_rows=[expected_vals],
        )
        storemgr.connect()
        res = storemgr.select_star("users")
        storemgr.close_conn()
        ass()
        assert res == [expected_dict]

    def test_select_star_where_equal(self, storemgr, mock_dbconnect):
        expected_query = ("SELECT * FROM users WHERE id = 'bg' AND "+
                          "first_name = 'billy' ")
        expected_cols = ('id', 'first_name', 'last_name')
        expected_vals = ('bg', 'billy', 'graham')
        expected_dict = {elem[0]: elem[1] for elem in zip(expected_cols, expected_vals)}
        ass = mock_dbconnect(
            expected_query=expected_query,
            expected_cols=expected_cols,
            expected_rows=[expected_vals],
        )
        storemgr.connect()
        res = storemgr.select_star_where_equal(
            "users", {"id": "bg", "first_name": "billy"})
        storemgr.close_conn()
        ass()
        assert res == [expected_dict]
