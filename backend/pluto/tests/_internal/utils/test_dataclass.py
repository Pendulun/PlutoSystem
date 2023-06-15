import pytest

from pluto._internal.utils.dataclass import validate_non_empty_string

def test_validate_non_empty_string():
    with pytest.raises(ValueError):
        s = ""
        validate_non_empty_string(s)
