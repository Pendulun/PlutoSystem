from typing import Any

import psycopg2

from pluto._internal.config.config import Config
from pluto._internal.log import log

logger = log.logger()


class StorageManager:
    def __init__(self, cfg: Config) -> None:
        self._cfg = cfg
        self._connstr = "user={} password={} host={} port={} dbname={}".format(
            cfg.dbuser,
            cfg.dbpassword,
            cfg.dbhost,
            cfg.dbport,
            cfg.dbname,
        )

    def insert(self, table: str, colvals: dict[str, Any]) -> list[Any]:
        if len(colvals) == 0:
            return []
        colstr = ""
        valstr = ""
        for col in colvals:
            colstr += f"{col}, "
            valstr += f"{self._fmtsqllit(colvals[col])}, "
        colstr = colstr[:-2]
        valstr = valstr[:-2]
        return self.query(f"INSERT INTO {table} ({colstr}) VALUES ({valstr})")

    def query(self, q: str) -> list[Any]:
        logger.debug("Querying database with string: {}".format(q))
        cur = self._conn.cursor()
        cur.execute(q)
        self._conn.commit()
        rows_clean: list[tuple[str]] = []
        if "SELECT" in q and cur.rowcount > 0:
            rows = cur.fetchall()
            rows_clean = list(map(lambda r: tuple(map(lambda s: s.strip(), r)), rows))  # type: ignore
        cur.close()
        return rows_clean

    def connect(self):
        logger.debug(f"Connecting to {self._cfg.dbname}")
        self._conn = psycopg2.connect(self._connstr)

    def close_conn(self):
        self._conn.close()

    ################################################################
    # Useful query patterns
    ################################################################

    # drop_table drops a SQL database table if it exists. Useful for testing.
    def drop_table(self, table: str):
        self.query(f"DROP TABLE IF EXISTS {table}")

    # creates_table drops a SQL database table if it does not exist. Useful for
    # testing.
    def create_table(self, table: str, coldef: dict[str, str]):
        q = f"CREATE TABLE IF NOT EXISTS {table}"
        q += "("
        for colName, colType in zip(coldef.keys(), coldef.values()):
            q += "{} {},".format(colName, colType)
        q = q[:-1]  # Remove last comma
        q += ")"
        self.query(q)

    # ping_table raises exception if table does not exist. Useful for testing.
    def ping_table(self, table: str):
        self.query(f"SELECT * FROM {table} LIMIT 0")

    # select_start selects all elements of a table. Useful mainly for testing.
    def select_star(self, table: str):
        return self.query(f"SELECT * FROM {table}")

    # select_star_where_equal selects all elements that match given conditions.
    def select_star_where_equal(self, table: str, conditions: dict[str, str]):
        q = "SELECT * FROM {} WHERE ".format(table)
        condkeys = conditions.keys()
        for i, k, v in zip(range(len(condkeys)), condkeys, conditions.values()):
            if i > 0:
                q += "AND {} = {} ".format(k, self._fmtsqllit(v))
        return self.query(q)

    # _fmtsqllit formats a sql literal, adding enclosing quotes etc as
    # necessary
    def _fmtsqllit(self, val: Any) -> str:
        if isinstance(val, str):
            return f"'{val}'"
        else:
            return val
