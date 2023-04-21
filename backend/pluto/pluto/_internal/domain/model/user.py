from dataclasses import asdict, dataclass

from pluto._internal.utils.id import new_id


@dataclass
class User:
    id: str
    first_name: str
    last_name: str

    dict = asdict

    @staticmethod
    def new(first_name: str, last_name: str) -> "User":
        # TODO: validate names -aholmquist 2023-04-14
        return User(new_id(), first_name, last_name)
