from abc import ABC, abstractmethod

from pluto._internal.domain.ports.database import Database


class IExpenseService(ABC):
    _expense_table = "expense"
    _expense_tag_table = "expense_tag"

    list_expense_filter_tag_name = "tag_name"
    list_expense_filters = [list_expense_filter_tag_name]

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    @abstractmethod
    def add_expense_from_dict_without_id(self, expense_dict: dict) -> None:
        pass

    @abstractmethod
    def add_expense_from_file(self, file_path: str, user_id: str) -> None:
        pass
