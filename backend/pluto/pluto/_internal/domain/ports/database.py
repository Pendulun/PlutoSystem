from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple

from pluto._internal.config.config import Config


class Database(ABC):
    def __init__(self, cfg: Config):
        self._cfg = cfg
        self._conn = None

    @abstractmethod
    def insert(self, table: str, colvals: dict[str, Any]) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def query(self, q: str) -> List[Dict[str, Any]]:
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
    def select_star(self, table: str) -> list[Any]:
        pass

    @abstractmethod
    def select_where_equal(
        self, cols: List[str], table: str, and_conditions: dict[str, str]
    ):
        pass

    @abstractmethod
    def select_star_where_equal(self, table: str, and_conditions: dict[str, str]):
        pass

    @abstractmethod
    def select_join_where_equal(
        self,
        cols: List[str],
        tables: Tuple[str, str],
        join_condition: Tuple[str, str],
        and_conditions: dict[str, str],
    ):
        pass
