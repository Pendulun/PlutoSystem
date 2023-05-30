from typing import Any, Dict, List, Tuple
from datetime import datetime

from pluto._internal.domain.ports.database import Database
from pluto._internal.config.config import Config
from pluto._internal.dash.utils import DashCallbacksUtil


class DashCallbacksUtilMock(DashCallbacksUtil):
    @classmethod
    def get_current_date(cls):
        return datetime.strptime("01/05/2023", "%d/%m/%Y")

class ConfigMock(Config):
    @staticmethod
    def parse() -> "Config":
        host = "host"
        port = 123
        dbuser = "db_user"
        dbpassword = "password"
        dbhost = "db_host"
        dbport = 42
        dbname = "db_name"

        return Config(
            host=host,
            port=port,
            dbuser=dbuser,
            dbpassword=dbpassword,
            dbhost=dbhost,
            dbport=dbport,
            dbname=dbname,
        )

class DatabaseMock(Database):

    def insert(self, table: str, colvals: dict[str, Any]) -> List[Dict[str, Any]]:
        pass

    def query(self, q: str) -> List[Dict[str, Any]]:
        pass

    def connect(self):
        pass

    def close_conn(self):
        pass

    def drop_table(self, table: str):
        pass

    def create_table(self, table: str, coldef: dict[str, str]):
        pass

    def ping_table(self, table: str):
        pass

    def select_star(self, table: str):
        pass

    def select_where_equal(
        self, cols: List[str], table: str, and_conditions: dict[str, str]
    ):
        pass

    def select_star_where_equal(self, table: str, and_conditions: dict[str, str]):
        pass

    def select_join_where_equal(
        self,
        cols: List[str],
        tables: Tuple[str, str],
        join_condition: Tuple[str, str],
        and_conditions: dict[str, str],
    ):
        pass

