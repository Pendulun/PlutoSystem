from abc import ABC, abstractmethod

from pluto._internal.domain.ports.database import Database


class IIncomeService(ABC):
    _income_table = "income"

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    @abstractmethod
    def add_income(self, income_dict: dict) -> None:
        pass