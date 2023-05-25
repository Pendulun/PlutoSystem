from abc import ABC, abstractmethod

from pluto._internal.domain.ports.database import Database


class IExpenseService(ABC):
    _expense_table = "expense"

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    @abstractmethod
    def add_expense_from_dict_without_id(self, expense_dict: dict) -> None:
        pass

    @abstractmethod
    def add_expense_from_file(self, file_path: str, user_id: str) -> None:
        pass
