from typing import Any


class StorageManager:
    def __init__(self, dbhost: str, dbport: int) -> None:
        self._dbhost = dbhost
        self._dbport = dbport

    def insert(self, table: str, colvals: dict[str, Any]) -> str:
        if len(colvals) == 0:
            return ""
        colstr = ""
        valstr = ""
        for col in colvals:
            colstr += f"{self._fmtsqllit(col)},"
            valstr += f"{self._fmtsqllit(colvals[col])},"
        colstr = colstr[:-1]
        valstr = valstr[:-1]
        return self.query(f"INSERT INTO {table} ({colstr}) VALUES ({valstr})")

    def query(self, q: str) -> str:
        return "TODO"

    def _fmtsqllit(self, val: Any) -> str:
        if isinstance(val, str):
            return f'"{val}"'
        else:
            return val
