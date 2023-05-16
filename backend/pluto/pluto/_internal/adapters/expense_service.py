from pluto._internal.domain.model.expense import Expense
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.ports.expense_service import IExpenseService


class ExpenseServiceImpl(IExpenseService):
    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def add_expense(self, expense_dict: dict) -> None:
        expense = Expense.new(**expense_dict)
        self._sm.insert(ExpenseServiceImpl._expense_table, expense.dict())
