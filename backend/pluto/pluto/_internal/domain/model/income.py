from dataclasses import asdict, dataclass

from pluto._internal.utils.id import new_id


@dataclass
class Income:
    id: str
    user_id: str
    src: str
    amount: int

    dict = asdict

    @staticmethod
    def new(user_id: str, src: str, amount: int) -> "Income":
        # TODO: validate -aholmquist 2023-04-14
        return Income(new_id(), user_id, src, amount)