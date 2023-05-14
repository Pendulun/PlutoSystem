from os import environ

import pytest

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

class TestConfig:
    def test_parse_not_all_set(self, empty_envvars):
        environ["HOST"] = "localhost"
        environ["PORT"] = "8057"
        with pytest.raises(KeyError):
            Config.parse()

    def test_parse_basic(self, basic_envvars):
        cfg = Config.parse()
        assert cfg.host == "localhost"
        assert cfg.port == 8999
        assert cfg.dbhost == "localhost"
        assert cfg.dbuser == "pluto_dog"
        assert cfg.dbpassword == "you-shall-not-pass"
        assert cfg.dbport == 1234
        assert cfg.dbname == "pluto"

