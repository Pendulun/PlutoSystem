from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Dict, List

from pluto._internal.utils.id import new_id


@dataclass
class Income:
    id: str
    user_id: str
    src: str
    amount: float
    inc_date: str

    dict = asdict

    @staticmethod
    def new(user_id: str, src: str, amount: float) -> Income:
        curr_date = datetime.today().strftime("%Y-%m-%d")
        return Income(new_id(), user_id, src, amount, curr_date)

    @staticmethod
    def from_complete_dict(income_dict: Dict) -> Income:
        """
        Expects a dict that has the following keys:
        id, user_id, src, amount, inc_date
        """
        return Income(**income_dict)

    @staticmethod
    def fields() -> List[str]:
        return [field_name for field_name in Income.__dataclass_fields__]

    def to_dict(self):
        my_dict = {
            "user_id": self.user_id,
            "id": self.id,
            "src": self.src,
            "amount": self.amount,
            "inc_date": self.inc_date.strftime("%Y-%m-%d"),
        }
        return my_dict
