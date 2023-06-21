from typing import Any, Dict, List

from pluto._internal.domain.model.income import Income
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.ports.income_service import IIncomeService
from pluto._internal.log import log

logger = log.logger()


class IncomeServiceImpl(IIncomeService):
    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def list_income(self, filters: Dict[str, Any]) -> List[Income]:
        if len(filters) == 0:
            income_dicts = self._sm.select_star(IIncomeService._income_table)
        else:
            income_dicts = self._sm.select_where_equal(
                cols=Income.fields(),
                table=IncomeServiceImpl._income_table,
                and_conditions=filters,
            )

        incomes = []
        if income_dicts is not None:
            incomes = [Income(**d) for d in income_dicts]

        return incomes

    def add_income(self, income_dict: dict) -> None:
        print(f"Adding income {income_dict}")
        curr_amount = income_dict["amount"]
        if isinstance(curr_amount, str):
            curr_amount = curr_amount.replace(",", ".")

        income_dict["amount"] = float(curr_amount)
        income = Income.new(**income_dict)
        self._sm.insert(IncomeServiceImpl._income_table, income.dict())

    def add_income_from_file(self, file_path: str, user_id: str) -> None:
        """
        Each file row should be src;amount
        Example: mercado;15.35
        """
        income_dicts: List[dict] = []
        contents = open(file_path).read()
        lines = [line for line in contents.split("\n") if line != ""]
        print(f"Read following lines from file {file_path}: {lines}")
        for i in range(len(lines)):
            row = lines[i]
            by_semicol = row.split(";")
            num_elems = 2
            if len(by_semicol) != num_elems:
                raise ValueError(
                    f"Row {i} of income file has invalid number of "
                    + f"elements. Expected {num_elems}, got "
                    + f"{len(by_semicol)}"
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
