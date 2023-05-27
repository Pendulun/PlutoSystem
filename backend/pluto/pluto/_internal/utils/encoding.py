import json
from typing import Any


def json_dumps(o: Any):
    return json.dumps(o, ensure_ascii=False)
