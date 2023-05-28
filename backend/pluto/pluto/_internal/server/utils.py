from typing import Any

from pluto._internal.utils.encoding import json_dumps


def dump_resp(resp: Any = dict()):
    return json_dumps(resp)
