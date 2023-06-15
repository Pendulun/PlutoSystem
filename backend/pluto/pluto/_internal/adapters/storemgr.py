from typing import Any, Dict, List, Tuple

import psycopg2

from pluto._internal.config.config import Config
from pluto._internal.domain.ports.database import Database
from pluto._internal.log import log

logger = log.logger()


class SQLStorageManager(Database):
    """
    This is a base class for all databases that uses SQL language.
    It doesn't implements the following methods:
    query(...)
    connect(...)
    close_conn(...)
    """

    def __init__(self, cfg: Config) -> None:
        super().__init__(cfg)

    def insert(self, table: str, colvals: dict[str, Any]) -> List[Dict[str, Any]]:
        print(f"Inserting into table {table} the vals {colvals}")
        if len(colvals) == 0:
            return list()
        colstr = ""
        valstr = ""
        for col in colvals:
            colstr += f"{col}, "
            valstr += f"{self._fmtsqllit(colvals[col])}, "
        colstr = colstr[:-2]
        valstr = valstr[:-2]
        return self.query(f"INSERT INTO {table} ({colstr}) VALUES ({valstr})")

    ################################################################
    # Useful query patterns
    ################################################################

    # drop_table drops a SQL database table if it exists. Useful for testing.
    def drop_table(self, table: str):
        self.query(f"DROP TABLE IF EXISTS {table}")

    # creates_table creates a SQL database table if it does not exist. Useful
    # for testing.
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
    def select_star(self, table: str) -> list[Any]:
        return self.query(f"SELECT * FROM {table}")

    def select_where_equal(
        self, cols: List[str], table: str, and_conditions: dict[str, str]
    ):
        q = "SELECT {} FROM {} WHERE ".format(self._fmtsqlcols(cols), table)
        q += self._where_equal_str(and_conditions)
        return self.query(q)

    # select_star_where_equal selects all elements that match given conditions.
    def select_star_where_equal(self, table: str, and_conditions: dict[str, str]):
        return self.select_where_equal(["*"], table, and_conditions)

    def select_join_where_equal(
        self,
        cols: List[str],
        tables: Tuple[str, str],
        join_condition: Tuple[str, str],
        and_conditions: dict[str, str],
    ):
        return self.select_where_equal(
            cols=cols,
            table=self._table_join_str(tables, join_condition),
            and_conditions=and_conditions,
        )

    # _table_join_str returns SQL syntax for the join of two tables.
    def _table_join_str(self, tables: Tuple[str, str], on_equals: Tuple[str, str]):
        return (
            f"{tables[0]} JOIN {tables[1]} ON "
            + f"{tables[0]}.{on_equals[0]} = {tables[1]}.{on_equals[1]}"
        )

    def _where_equal_str(self, and_conditions: dict[str, str]) -> str:
        s = ""
        condkeys = and_conditions.keys()
        for i, k, v in zip(range(len(condkeys)), condkeys, and_conditions.values()):
            if i == 0:
                s += "{} = {} ".format(k, self._fmtsqllit(v))
            else:
                s += "AND {} = {} ".format(k, self._fmtsqllit(v))
        return s

    # _fmtsqllit formats a sql literal, adding enclosing quotes etc as
    # necessary
    def _fmtsqllit(self, val: Any) -> str:
        if isinstance(val, str):
            return f"'{val}'"
        else:
            return val

    # _fmtsqlcols formats a list of column names into sql syntax.
    def _fmtsqlcols(self, cols: List[str]) -> str:
        if len(cols) == 0:
            return "*"
        if len(cols) == 1:
            return cols[0]
        s = cols[0]
        for col in cols[1:]:
            s += f", {col}"
        return s

    def _cursor_col_names(self, cur) -> list[str]:
        if cur.description is None:
            return []
        cols: list[str] = []
        for cur_col in cur.description:
            cols.append(cur_col.name)
        return cols


class PGSQLStorageManager(SQLStorageManager):
    def __init__(self, cfg: Config) -> None:
        super().__init__(cfg)
        self._connstr = "user={} password={} host={} port={} dbname={}".format(
            self._cfg.dbuser,
            self._cfg.dbpassword,
            self._cfg.dbhost,
            self._cfg.dbport,
            self._cfg.dbname,
        )

    # Methods that must be overriden
    def query(self, q: str) -> List[Dict[str, Any]]:
        print("Querying database with string: {}".format(q))
        if not self._conn:
            raise ValueError(
                "Database has no connection! Must explicit call connect() before queries!"
            )
        cur = self._conn.cursor()
        cur.execute(q)
        cols = self._cursor_col_names(cur)
        self._conn.commit()
        rows_clean: list[tuple[str]] = []
        if "SELECT" in q and cur.rowcount > 0:
            rows = cur.fetchall()
            rows_clean = list(
                map(
                    lambda r: tuple(
                        map(lambda s: s.strip() if isinstance(s, str) else s, r)
                    ),
                    rows,
                )
            )  # type: ignore
        cur.close()
        rows_dicts: List[Dict[str, Any]] = []
        for row in rows_clean:
            newdict = dict()
            for i in range(len(row)):
                key = cols[i]
                val = row[i]
                newdict[key] = val
            rows_dicts.append(newdict)
        return rows_dicts

    def connect(self):
        print(f"Connecting to {self._cfg.dbname}")
        self._conn = psycopg2.connect(self._connstr)

    def close_conn(self):
        self.__del__()

    def __del__(self):
        if self._conn:
            self._conn.close()
