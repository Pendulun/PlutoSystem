import pytest
import pathlib

from pluto._internal.adapters.income_service import IncomeServiceImpl
from pluto._internal.utils.id import new_id

from tests._internal.mocks import DatabaseMock, ConfigMock

class TestIncomeService:
    @pytest.fixture
    def income_service(self):
        return IncomeServiceImpl(DatabaseMock(ConfigMock.parse()))

    @pytest.fixture
    def real_income_service(self, real_storemgr_configured):
        return IncomeServiceImpl(real_storemgr_configured)

    def test_add_income_file_wrong_num_cols(self, income_service):
        invalid_num_cols_file = pathlib.Path("tests/fixtures/income_invalid.csv")
        user_id = '1'
        with pytest.raises(ValueError) as e:
            income_service.add_income_from_file(invalid_num_cols_file, user_id)

    @pytest.mark.integtest
    def test_list_income(self, real_income_service):
        oneline_file = pathlib.Path("tests/fixtures/incomes_valid.csv")
        user_id = "putin"
        real_income_service.add_income_from_file(oneline_file, user_id)
        incomes = real_income_service.list_income({})
        assert len(incomes) == 2

    @pytest.mark.integtest
    def test_add_income_file(
            self,
            real_income_service,
            putin_user,
            bj_user,
    ):
        oneline_file = pathlib.Path("tests/fixtures/incomes_valid.csv")
        user_id = "putin"
        real_income_service.add_income_from_file(oneline_file, user_id)
        rows = real_income_service._sm.select_star("income")
        assert len(rows) == 2
        income1 = rows[0]
        assert income1["user_id"] == user_id
        assert income1["src"] == "mercado"
        assert income1["amount"] == 15.5
        income2 = rows[1]
        assert income2["user_id"] == user_id
        assert income2["src"] == "mercado2"
        assert income2["amount"] == 30.5
        # Cleanup
        real_income_service._sm.query(
            f"DELETE FROM income WHERE id = '{income1['id']}' or id = '{income2['id']}'",
        )
