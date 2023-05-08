from pluto._internal.domain.ports.database import Database
from abc import ABC, abstractmethod

class IExpenseService(ABC):
    _expense_table = "expense"

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    @abstractmethod
    def add_expense(self, expense_dict:dict) -> None:
        pass
