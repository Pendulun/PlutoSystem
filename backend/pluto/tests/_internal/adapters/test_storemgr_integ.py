import psycopg2
import pytest


class TestStorageManager:
    @pytest.fixture
    def real_storemgr_configured(self, real_storemgr, users_table):
        real_storemgr.create_table("users", users_table)
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
        expected = [
            {"id": "putin", "name": "vladimir putin", "email": "putin@massacre.death",
             "password": "123"},
            {"id": "bj", "name": "b j", "email": "bj@b.j", "password": "321"},
        ]
        actual = real_storemgr_configured.select_star("users")
        assert actual == expected
