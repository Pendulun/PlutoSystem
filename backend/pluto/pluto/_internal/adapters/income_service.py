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

    def add_income_from_file(self, file_path: str, user_id: str) -> None:
        """
        Each file row should be src;amount
        Example: mercado;15.35
        """
        income_dicts: List[dict] = []
        contents = open(file_path).read()
        lines = contents.split("\n")
        for i in range(len(lines)):
            row = lines[i]
            by_semicol = row.split(";")
            num_elems = 2
            if len(by_semicol) != num_elems:
                raise ValueError(
                    f"Row {i} of income file has invalid number of "
                    + f"elements. Expected {num_elems}, got "
                    + "{len_bysemicol}"
                )
            income_dicts.append(
                dict(
                    user_id=user_id,
                    src=by_semicol[0],
                    amount=float(by_semicol[1]),
                )
            )
        for income_dict in income_dicts:
            self.add_income(income_dict)

    def incomes_from_user_id(self, user_id: str) -> list[Income]:
        conditions = {"user_id": user_id}
        results = self._sm.select_star_where_equal(
            IncomeServiceImpl._income_table, conditions
        )
        return [Income.from_complete_dict(result) for result in results]
