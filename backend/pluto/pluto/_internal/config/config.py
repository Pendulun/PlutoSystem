from dataclasses import dataclass, field
from os import environ

from pluto._internal.utils.dataclass import validate_non_empty_string


@dataclass
class Config:
    host: str = field(
        default="localhost", metadata={"validate": validate_non_empty_string}
    )
    port: int = 8057
    dbuser: str = field(default="", metadata={"validate": validate_non_empty_string})
    dbpassword: str = field(
        default="", metadata={"validate": validate_non_empty_string}
    )
    dbhost: str = field(default="", metadata={"validate": validate_non_empty_string})
    dbport: int = 5432
    dbname: str = field(default="", metadata={"validate": validate_non_empty_string})

    @staticmethod
    def parse() -> "Config":
        host = environ["HOST"]
        port = int(environ["PORT"])
        dbuser = environ["DB_USER"]
        dbpassword = environ["DB_PASSWORD"]
        dbhost = environ["DB_HOST"]
        dbport = int(environ["DB_PORT"])
        dbname = environ["DB_NAME"]

        return Config(
            host=host,
            port=port,
            dbuser=dbuser,
            dbpassword=dbpassword,
            dbhost=dbhost,
            dbport=dbport,
            dbname=dbname,
        )

    def as_dict(self) -> dict:
        config_dict = {
            "host": self.host,
            "port": self.port,
            "dbuser": self.dbuser,
            "dbpassword": self.dbpassword,
            "dbhost": self.dbhost,
            "dbport": self.dbport,
            "dbname": self.dbname,
        }
        return config_dict
