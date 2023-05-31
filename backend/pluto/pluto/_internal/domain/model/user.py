from dataclasses import asdict, dataclass

from pluto._internal.utils.id import new_id


@dataclass
class User:
    id: str
    name: str
    email: str
    password: str

    dict = asdict

    @staticmethod
    def new(name: str, email: str, password: str) -> "User":
        # TODO: validate names -aholmquist 2023-04-14
        return User(new_id(), name, email, password)
