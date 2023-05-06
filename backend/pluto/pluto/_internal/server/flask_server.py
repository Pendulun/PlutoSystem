from __future__ import annotations

from flask import Flask, request, make_response

from pluto._internal.config.config import Config
from pluto._internal.server.server import Server
from pluto._internal.domain.ports.database import Database
from pluto._internal.domain.model.expense import Expense
from pluto._internal.domain.model.income import Income

from typing import Callable
import random
import requests


#Based on:
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-5cb
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-part-2-4507
def make_flask_server(config: Config, database:Database) -> Server:
    flask_app = Flask('pluto')
    server = FlaskServerWrapper(flask_app, config, database)
    return server

class EndpointHandler(object):

    def __init__(self, action):
        self.action = action 

    def __call__(self, *args, **kwargs):
        response = self.action(*args, **request.view_args)
        return make_response(response)

class FlaskServerWrapper(Server):

    def __init__(self, app:Flask, config:Config, database:Database):
        super().__init__(config)
        self.app = app
        self.db = database
        self.configs(self._cfg)
        self._add_endpoints()

    def configs(self, config:Config):
        for config, value in config.as_dict().items():
            self.app.config[config.upper()] = value
    
    def _add_endpoints(self):
        #example endpoint
        self.add_endpoint('/action/<string:name>', 'action', self.action)
        
        self.add_endpoint('/expenses/add/','add_expenses', self.add_expense, methods=['POST'])
        self.add_endpoint('/incomes/add/', 'add_income', self.add_income, methods=['POST'])
        #testing functions
        self.add_endpoint('/make_expense/', 'make_expense', self.request_add_random_expense)
        self.add_endpoint('/make_income/', 'make_income', self.request_add_random_income)

    def add_endpoint(self, endpoint:str=None, endpoint_name:str=None, handler:Callable=None, methods:list=None, *args, **kwargs):
        if methods is None:
            methods = ['GET']
        
        self.app.add_url_rule(endpoint, endpoint_name, EndpointHandler(handler), methods=methods, *args, **kwargs)

    #example action
    def action(self, name):
        """
        This function takes `name` argument and returns `Hello <name>`.
        """
        return "Hello " + name

    # testing methods
    def request_add_random_expense(self):
        dictToSend = {
            'user_id':random.randint(0, 1000), 
            'src':'mercadao', 
            'amount':random.random()*100
            }
        res = requests.post('http://localhost:5000/expenses/add/', json=dictToSend)
        return res.content
    
    def request_add_random_income(self):
        dictToSend = {
            'user_id':random.randint(0, 1000), 
            'src':'salario', 
            'amount':random.random()*10000
            }
        print('chegou aqui ')
        res = requests.post('http://localhost:5000/incomes/add/', json=dictToSend)
        return res.content
    
    def run(self, **kwargs):
        self.app.run(debug=True, **kwargs)
    
    def add_expense(self):
        expense_dict = request.get_json(force=True) 
        new_expense = Expense.new(**expense_dict)
        self.db.insert(Expense.table(), new_expense.dict())
        return f"Inseriu {expense_dict} com sucesso!"

    def add_income(self):
        income_dict = request.get_json(force=True) 
        new_income = Income.new(**income_dict)
        self.db.insert(Income.table(), new_income.dict())
        return f"Inseriu {new_income} com sucesso!"