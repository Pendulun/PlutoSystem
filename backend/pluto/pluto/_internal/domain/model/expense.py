from dataclasses import asdict, dataclass

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
