from pluto._internal.adapters.storemgr import StorageManager
from pluto._internal.domain.model.user import User


class UserService:
    _user_table = "users"

    def __init__(self, sm: StorageManager) -> None:
        self._sm = sm

    def add_user(self, user: User) -> None:
        self._sm.insert(UserService._user_table, user.dict())
