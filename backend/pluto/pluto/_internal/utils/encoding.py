import dataclasses
import json
from typing import Any


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def json_dumps(o: Any):
    return json.dumps(o, cls=EnhancedJSONEncoder, ensure_ascii=False)
