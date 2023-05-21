import csv
import pathlib
from typing import List, Tuple

from pluto._internal.domain.model.expense import Expense
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.ports.expense_service import IExpenseService


class InvalidRow(Exception):
    pass


class ExpenseServiceImpl(IExpenseService):
    def __init__(self, sm: Database) -> None:
        super().__init__(sm)

    def add_expense_from_dict_without_id(self, expense_dict: dict) -> None:
        expense = Expense.new(**expense_dict)
        self.add_expense(expense)

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
                # Call method to add tag to expense
                pass

    def _extract_expenses_and_tags_from_file(
        self, user_id, file
    ) -> List[Tuple[Expense, List[str]]]:
        """
        Returns a list of tuples of form: ((1), (2))
            (1) A Expense instance
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
