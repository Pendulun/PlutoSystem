from __future__ import annotations
from pluto._internal.config.config import Config

import enum

class ServerTypeError(Exception):
    pass

class ServerType(enum.Enum):
    FLASK = 1

def make_server(type:ServerType, config: Config) -> Server:
    if type == ServerType.FLASK:
        #Only import if needed
        from pluto._internal.server.flask_server import make_flask_server
        return make_flask_server(config)
    else:
        raise ServerTypeError("Server Type not defined!")

class Server:
    def __init__(self, cfg: Config) -> None:
        self._cfg = cfg

    def run(self, **kwargs):
        raise NotImplementedError("Server run is not implemented!")