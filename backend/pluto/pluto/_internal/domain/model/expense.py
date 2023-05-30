from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Dict, List

from pluto._internal.utils.id import new_id


@dataclass
class Expense:
    id: str
    user_id: str
    src: str
    amount: float
    exp_date: str

    dict = asdict

    @staticmethod
    def new(user_id: str, src: str, amount: float) -> "Expense":
        curr_date = datetime.today().strftime("%d/%m/%Y")
        return Expense(new_id(), user_id, src, amount, curr_date)

    @staticmethod
    def fields() -> List[str]:
        return [field_name for field_name in Expense.__dataclass_fields__]

    @classmethod
    def from_complete_dict(cls, expense_dict: Dict) -> "Expense":
        """
        Expects a dict that has the following keys:
        id, user_id, src, amount, exp_date
        """
        return Expense(**expense_dict)
