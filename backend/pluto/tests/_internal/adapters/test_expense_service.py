import pytest
import pathlib

from pluto._internal.adapters.expense_service import ExpenseServiceImpl, InvalidRow

from tests._internal.mocks import DatabaseMock, ConfigMock

class TestExpenseService:

    @pytest.fixture
    def expense_service(self):
        return ExpenseServiceImpl(DatabaseMock(ConfigMock.parse()))

    def test_raises_invalid_num_cols(self, expense_service):
        invalid_num_cols_file = pathlib.Path("tests/fixtures/expense1.csv")
        user_id = '1'
        with pytest.raises(InvalidRow) as e:
            expense_service.add_expense_from_file(invalid_num_cols_file, user_id)
    
    def test_raises_empty_first_col(self, expense_service):
        invalid_num_cols_file = pathlib.Path("tests/fixtures/expense2.csv")
        user_id = '1'
        with pytest.raises(ValueError) as e:
            expense_service.add_expense_from_file(invalid_num_cols_file, user_id)
    
    def test_raises_wrong_type_for_amount(self, expense_service):
        invalid_num_cols_file = pathlib.Path("tests/fixtures/expense3.csv")
        user_id = '1'
        with pytest.raises(TypeError) as e:
            expense_service.add_expense_from_file(invalid_num_cols_file, user_id)
    
    def test_dont_raise_for_valid_entries(self, expense_service):
        valid_file = pathlib.Path("tests/fixtures/expense4.csv")
        user_id = '1'
        try:
            expense_service.add_expense_from_file(valid_file, user_id)
        except Exception as e:
            assert False, f"valid expense file raised an exception {e}"
