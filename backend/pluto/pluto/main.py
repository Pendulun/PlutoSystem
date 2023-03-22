import sys

from pluto._internal.config.config import Config
from pluto._internal.log import log
from pluto._internal.server.server import Server

logger = log.logger()


def main():
    try:
        try:
            config = Config.parse(sys.argv[1:])
            server = Server(config)
        except Exception as e:
            logger.critical(f"Failed to initialize server: {e}", exc_info=True)
            return

        server.run()
    except Exception as e:
        logger.critical(f"Unrecoverable error: {e}", exc_info=True)
        return


if __name__ == "__main__":
    main()
