from pluto._internal.domain.model.user import User
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.ports.user_service import IUserService


class UserServiceImpl(IUserService):
    def __init__(self, sm: Database) -> None:
        self._sm = sm

    def add_user(self, user_dict: dict) -> None:
        user = User.new(**user_dict)
        self._sm.insert(IUserService._user_table, user.dict())

    def get_user(self, email: str) -> User:
        return self._sm.select_star_where_equal(
            table=UserServiceImpl._user_table,
            and_conditions=dict(email=email),
        )
