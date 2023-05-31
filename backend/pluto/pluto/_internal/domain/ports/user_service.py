from abc import ABC, abstractmethod

from pluto._internal.domain.model.user import User
from pluto._internal.domain.ports.database import Database


class IUserService(ABC):
    _user_table = "users"

    def __init__(self, sm: Database) -> None:
        self._sm = sm

    @abstractmethod
    def get_user(self, email: str) -> User:
        pass

    @abstractmethod
    def add_user(self, user_dict: dict) -> None:
        pass
