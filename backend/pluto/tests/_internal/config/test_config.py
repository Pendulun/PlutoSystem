import pytest

from pluto._internal.config.config import Config
from pluto._internal.config.error import InvalidConfigError


class TestConfig:
    def test_parse_empty(self):
        with pytest.raises(InvalidConfigError):
            Config.parse([])

    def test_parse_just_one(self):
        with pytest.raises(InvalidConfigError):
            Config.parse(["something"])

    def test_parse_basic(self):
        host = "localhost"
        port = 8057
        config = Config.parse(
            [
                host,
                port,
            ]
        )
        assert config.host == host
        assert config.port == port
