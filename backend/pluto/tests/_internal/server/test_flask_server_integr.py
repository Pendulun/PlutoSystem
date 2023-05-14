import pytest
from pluto._internal.server.flask_server import make_flask_server, FlaskServerWrapper
from pluto._internal.config.config import Config
from pluto._internal.domain.ports.database import Database
import random
import requests
from typing import Any

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

class DatabaseMock(Database):
    def insert(self, table: str, colvals: dict[str, Any]) -> list[Any]:
        pass

    def query(self, q: str) -> list[Any]:
        pass

    def connect(self):
        pass

    def close_conn(self):
        pass

    def drop_table(self, table: str):
        pass

    def create_table(self, table: str, coldef: dict[str, str]):
        pass

    def ping_table(self, table: str):
        pass

    def select_star(self, table: str):
        pass

    def select_star_where_equal(self, table: str, and_conditions: dict[str, str]):
        pass
    
class TestFlaskServer:

    def fixture(self):
        # testing functions
        self.server:FlaskServerWrapper = make_flask_server(ConfigMock.parse(), DatabaseMock())
        self.server.add_endpoint(
            "/make_expense/", "make_expense", self.request_add_random_expense
        )
        self.server.add_endpoint(
            "/make_income/", "make_income", self.request_add_random_income
        )

        self.server.run()

    def down(self):
        #Eu só achei um jeito de desligar o servidor: apertando ctr+c
        pass

    # testing methods
    def request_add_random_expense(self):
        dictToSend = {
            "user_id": random.randint(0, 1000),
            "src": "mercadao",
            "amount": random.random() * 100,
        }
        res = requests.post("http://localhost:5000/expenses/", json=dictToSend)
        return res.content

    def request_add_random_income(self):
        dictToSend = {
            "user_id": random.randint(0, 1000),
            "src": "salario",
            "amount": random.random() * 10000,
        }
        print("chegou aqui ")
        res = requests.post("http://localhost:5000/incomes/", json=dictToSend)
        return res.content

    #real tests