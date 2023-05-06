from typing import Any
from pluto._internal.config.config import Config
from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self, cfg: Config):
        self._cfg = cfg
        self._conn = None
    
    @abstractmethod
    def insert(self, table: str, colvals: dict[str, Any]) -> list[Any]:
        pass

    @abstractmethod
    def query(self, q: str) -> list[Any]:
        pass
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close_conn(self):
        pass

    @abstractmethod
    def drop_table(self, table: str):
        pass

    @abstractmethod
    def create_table(self, table: str, coldef: dict[str, str]):
        pass
    
    @abstractmethod
    def ping_table(self, table: str):
        pass

    @abstractmethod
    def select_star(self, table: str):
        pass

    @abstractmethod
    def select_star_where_equal(self, table: str, and_conditions: dict[str, str]):
        pass