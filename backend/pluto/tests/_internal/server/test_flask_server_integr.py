import pytest
from pluto._internal.server.flask_server import make_flask_server, FlaskServerWrapper
from tests._internal.mocks import ConfigMock, DatabaseMock
import random
import requests
    
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

        self.server.add_endpoint("/action/<string:name>", "action", self.action)

        self.server.run()

    def down(self):
        #Eu só achei um jeito de desligar o servidor: apertando ctr+c
        pass

    # testing reqs

    def action(self, name):
        """
        This function takes `name` argument and returns `Hello <name>`.
        """
        return "Hello " + name
    
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