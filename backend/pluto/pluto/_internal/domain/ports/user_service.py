from pluto._internal.domain.model.user import User
from pluto._internal.domain.ports.database import Database


class UserService:
    _user_table = "users"

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    def add_user(self, user: User) -> None:
        self._sm.insert(UserService._user_table, user.dict())
