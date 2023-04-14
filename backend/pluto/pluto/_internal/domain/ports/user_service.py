from pluto._internal.adapters.storemgr import StorageManager
from pluto._internal.domain.model.user import User


class UserService:
    def __init__(self, sm: StorageManager) -> None:
        self._sm = sm

    def add_user(self, user: User) -> None:
        self._sm.insert(user.table(), user.dict())
