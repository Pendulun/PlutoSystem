import csv
import pathlib
from typing import Any, Dict, List, Tuple

from pluto._internal.domain.model.expense import Expense
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.ports.expense_service import IExpenseService


class InvalidRow(Exception):
    pass


class ExpenseServiceImpl(IExpenseService):
    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def list_expense(
        self, filters: Dict[str, Any]
    ) -> IExpenseService.ListExpenseResponse:
        if len(filters) == 0:
            expense_dicts = self._sm.select_star(ExpenseServiceImpl._expense_table)
        else:
            expense_dicts = self._sm.select_join_where_equal(
                cols=Expense.fields(),
                tables=(
                    ExpenseServiceImpl._expense_table,
                    ExpenseServiceImpl._expense_tag_table,
                ),
                join_condition=("id", "expense_id"),
                and_conditions=filters,
            )
        
        expenses = []
        if expense_dicts is not None:
            expenses = [Expense(**d) for d in expense_dicts]

        resp = {
            "expenses": expenses,
            "filters": filters,
        }

        return resp

    def add_expense_from_dict_without_id(self, expense_dict: dict) -> str:
        "Returns the expense id"
        expense = Expense.new(**expense_dict)
        self.add_expense(expense)
        return expense.id

    def add_expense(self, expense: Expense):
        self._sm.insert(ExpenseServiceImpl._expense_table, expense.dict())

    def add_expense_from_file(self, file_path: str, user_id: str) -> None:
        """
        Each file row should be src;amount;tags
        Example: mercado;15.35;tag1,tag2,tag3
        """
        file = pathlib.Path(file_path)

        expenses_and_tags_to_add = self._extract_expenses_and_tags_from_file(
            user_id, file
        )

        for expense, tags in expenses_and_tags_to_add:
            self.add_expense(expense)
            for tag in tags:
                self.add_tag_for_expense(tag, expense.id)

    def _extract_expenses_and_tags_from_file(
        self, user_id, file
    ) -> List[Tuple[Expense, List[str]]]:
        """
        Returns a list of tuples of form: ((1), (2))
            (1) An Expense instance
            (2) A list of tags
        """
        expenses_and_tags_to_add = list()
        with open(file) as expenses_file:
            csv_reader = csv.reader(expenses_file, delimiter=";")

            for expense_row in csv_reader:
                if not self._have_enough_cols(expense_row):
                    raise InvalidRow(
                        f"Quantidade de elementos na linha {expense_row} é inválido.\
                                     São necessários, pelo menos, duas colunas separadas por ponto e vírgula (;)."
                    )

                tags = list()
                # tags col separated by commas
                if len(expense_row) == 3:
                    tags = expense_row[2].split(",")
                    tags = list(filter(lambda a: len(a.strip()) > 0, tags))

                expense_dict = self._expense_dict_from_row(user_id, expense_row)
                expense = Expense.new(**expense_dict)

                expense_and_its_tags = (expense, tags)
                expenses_and_tags_to_add.append(expense_and_its_tags)

        return expenses_and_tags_to_add

    def _have_enough_cols(self, expense_row):
        return len(expense_row) >= 2

    def _expense_dict_from_row(self, user_id, expense_row) -> dict:
        expense_dict = {"user_id": user_id}
        expense_dict["src"] = expense_row[0].strip()
        if expense_dict["src"] == "":
            raise ValueError(
                f"Linha {expense_row}: Primeira coluna não pode ser vazia!"
            )

        try:
            expense_dict["amount"] = float(expense_row[1].replace(",", "."))
        except Exception:
            raise TypeError(
                f"Linha {expense_row}: '{expense_row[1]}' não é um valor de gasto válido!"
            )

        return expense_dict

    def expenses_from_user_id(self, user_id: str) -> list[Expense]:
        conditions = {"user_id": user_id}
        results = self._sm.select_star_where_equal(
            ExpenseServiceImpl._expense_table, conditions
        )
        return [Expense.from_complete_dict(result) for result in results]

    def add_tag_for_expense(self, tag_name: str, exp_id: str) -> None:
        self._sm.insert("expense_tag", {"expense_id": exp_id, "tag_name": tag_name})
