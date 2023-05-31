from abc import ABC, abstractmethod
from typing import Any, Dict, List

from pluto._internal.domain.model.income import Income
from pluto._internal.domain.ports.database import Database


class IIncomeService(ABC):
    _income_table = "income"

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    @abstractmethod
    def list_income(self, filters: Dict[str, Any]) -> List[Income]:
        pass

    @abstractmethod
    def add_income(self, income_dict: dict) -> None:
        pass

    @abstractmethod
    def add_income_from_file(self, file_path: str, user_id: str) -> None:
        pass

    @abstractmethod
    def incomes_from_user_id(self, user_id: str) -> list[Income]:
        pass
