from pluto._internal.domain.ports.expense_service import IExpenseService
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.model.expense import Expense

class ExpenseServiceImpl(IExpenseService):

    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def add_expense(self, user_dict:dict) -> None:
        expense = Expense.new(**user_dict)
        self._sm.insert(ExpenseServiceImpl._expense_table, expense.dict())