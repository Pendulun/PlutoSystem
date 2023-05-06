import sys

from pluto._internal.config.config import Config, ConfigMock
from pluto._internal.log import log
from pluto._internal.server.server import make_server, ServerType
from pluto._internal.adapters.storemgr import PGSQLStorageManager

logger = log.logger()


def main():
    try:
        try:
            config = Config.parse()
            server_type = ServerType.FLASK
            database = PGSQLStorageManager(config)
            database.connect()
            server = make_server(server_type, config, database)
        except Exception as e:
            logger.critical(f"Failed to initialize server: {e}", exc_info=True)
            return

        server.run()
    except Exception as e:
        logger.critical(f"Unrecoverable error: {e}", exc_info=True)
    finally:
        database.close_conn()

if __name__ == "__main__":
    main()
