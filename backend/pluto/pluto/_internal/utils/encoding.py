import dataclasses
import json
from typing import Any

from pluto._internal.domain.model.expense import Expense
from pluto._internal.domain.model.income import Income


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Income) or isinstance(o, Expense):
            return o.to_dict()

        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def json_dumps(o: Any):
    return json.dumps(o, cls=EnhancedJSONEncoder, ensure_ascii=False)
