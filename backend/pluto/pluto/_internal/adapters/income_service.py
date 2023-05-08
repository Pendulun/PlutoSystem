from pluto._internal.domain.ports.income_service import IIncomeService
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.model.income import Income

class IncomeServiceImpl(IIncomeService):

    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def add_income(self, income_dict:dict) -> None:
        income = Income.new(**income_dict)
        self._sm.insert(IncomeServiceImpl._income_table, income.dict())