from typing import List

from pluto._internal.domain.model.income import Income
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.ports.income_service import IIncomeService


class IncomeServiceImpl(IIncomeService):
    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def list_income(self) -> List[Income]:
        return self._sm.select_star(IncomeServiceImpl._income_table)

    def add_income(self, income_dict: dict) -> None:
        income = Income.new(**income_dict)
        self._sm.insert(IncomeServiceImpl._income_table, income.dict())
