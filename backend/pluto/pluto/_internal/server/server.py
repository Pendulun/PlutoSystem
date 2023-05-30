from __future__ import annotations

import enum

from pluto._internal.config.config import Config
from pluto._internal.domain.ports.database import Database


class ServerTypeError(Exception):
    pass


class ServerType(enum.Enum):
    FLASK = 1


def make_server(type: ServerType, config: Config, database: Database) -> Server:
    if type == ServerType.FLASK:
        # Only import if needed
        from pluto._internal.server.flask_server import make_flask_server

        return make_flask_server(config, database)
    else:
        raise ServerTypeError("Server Type not defined!")


class Server:
    DB_IMP: Database

    def __init__(self, cfg: Config) -> None:
        self._cfg = cfg

    def run(self, **kwargs):
        raise NotImplementedError("Server run is not implemented!")
