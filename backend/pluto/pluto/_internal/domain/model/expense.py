from dataclasses import asdict, dataclass
from typing import List

from pluto._internal.utils.id import new_id


@dataclass
class Expense:
    id: str
    user_id: str
    src: str
    amount: float

    dict = asdict

    @staticmethod
    def new(user_id: str, src: str, amount: float) -> "Expense":
        return Expense(new_id(), user_id, src, amount)

    @staticmethod
    def fields() -> List[str]:
        return [field_name for field_name in Expense.__dataclass_fields__]
