import psycopg2
import pytest


from pluto._internal.adapters.storemgr import PGSQLStorageManager

class TestStorageManager:
    @pytest.fixture
    def real_storemgr(self, basic_config, setup_real_pg):
        storemgr = PGSQLStorageManager(basic_config)
        storemgr._conn = psycopg2.connect(**setup_real_pg.dsn())
        return storemgr

    @pytest.fixture
    def real_storemgr_configured(self, real_storemgr):
        real_storemgr.create_table("users", dict(
            id="char(32)",
            first_name="char(32)",
            last_name="char(32)",
        ))
        return real_storemgr

    @pytest.mark.integtest
    def test_basic_config_real(self, real_storemgr_configured):
        pass

    @pytest.mark.integtest
    def test_drop_table(self, real_storemgr_configured):
        real_storemgr_configured.drop_table("users")
        with pytest.raises(psycopg2.errors.UndefinedTable):
            real_storemgr_configured.select_star("users")

    @pytest.mark.integtest
    def test_insert_two_users_then_select_all(
            self, real_storemgr_configured, putin_user, bj_user,
    ):
        real_storemgr_configured.insert("users", putin_user)
        real_storemgr_configured.insert("users", bj_user)
        rows = real_storemgr_configured.select_star("users")
        assert rows == [('putin', 'vladimir', 'putin'), ('bj', 'b', 'j')]
