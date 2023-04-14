from dataclasses import dataclass

from pluto._internal.config.error import InvalidConfigError


@dataclass
class Config:
    host: str
    port: int
    dbhost: str
    dbport: int

    _REQUIRED_NUM_ARGS = 4

    @staticmethod
    def parse(cli_args: list[str]) -> "Config":
        # Currently we require CLI arguments for simplicity.
        if len(cli_args) != Config._REQUIRED_NUM_ARGS:
            raise InvalidConfigError(
                "expected {} arguments, but got {}".format(
                    Config._REQUIRED_NUM_ARGS, len(cli_args)
                )
            )

        host = cli_args[0]
        port = int(cli_args[1])
        dbhost = cli_args[2]
        dbport = int(cli_args[3])

        return Config(
            host=host,
            port=port,
            dbhost=dbhost,
            dbport=dbport,
        )
