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
        dbuser = environ["DBUSER"]
        dbpassword = environ["DBPASSWORD"]
        dbhost = environ["DBHOST"]
        dbport = int(environ["DBPORT"])
        dbname = environ["DBNAME"]

        return Config(
            host=host,
            port=port,
            dbuser=dbuser,
            dbpassword=dbpassword,
            dbhost=dbhost,
            dbport=dbport,
            dbname=dbname,
        )
