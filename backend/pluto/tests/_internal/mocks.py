from typing import Any, Dict

from pluto._internal.domain.ports.database import Database
from pluto._internal.config.config import Config

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

    def insert(self, table: str, colvals: dict[str, Any]) -> Dict[str, Any]:
        pass

    def query(self, q: str) -> Dict[str, Any]:
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

    def select_star_where_equal(self, table: str, and_conditions: dict[str, str]):
        pass
