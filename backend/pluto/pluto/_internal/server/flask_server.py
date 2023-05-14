from __future__ import annotations

import random
from typing import Callable

import requests
from flask import Flask, make_response, request

from pluto._internal.adapters.expense_service import ExpenseServiceImpl
from pluto._internal.adapters.income_service import IncomeServiceImpl
from pluto._internal.config.config import Config
from pluto._internal.domain.ports.database import Database
from pluto._internal.server.server import Server


# Based on:
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-5cb
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-part-2-4507
def make_flask_server(config: Config, database: Database) -> Server:
    flask_app = Flask("pluto")
    server = FlaskServerWrapper(flask_app, config, database)
    return server


class EndpointHandler(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, *args, **kwargs):
        response = self.action(*args, **request.view_args)
        return make_response(response)


class FlaskServerWrapper(Server):
    def __init__(self, app: Flask, config: Config, database: Database):
        super().__init__(config)
        self.app = app
        self.db = database
        self.configs(self._cfg)
        self._add_endpoints()

    def configs(self, config: Config):
        for config_name, value in config.as_dict().items():
            self.app.config[config_name.upper()] = value

    def _add_endpoints(self):

        self.add_endpoint(
            "/expenses/", "add_expenses", self.add_expense, methods=["POST"]
        )
        self.add_endpoint(
            "/incomes/", "add_income", self.add_income, methods=["POST"]
        )

    def add_endpoint(
        self,
        endpoint: str,
        endpoint_name: str,
        handler: Callable,
        methods: list = ["GET"],
        *args,
        **kwargs,
    ):
        if methods is None:
            methods = ["GET"]

        self.app.add_url_rule(
            endpoint,
            endpoint_name,
            EndpointHandler(handler),
            methods=methods,
            *args,
            **kwargs,
        )

    def run(self, **kwargs):
        self.app.run(debug=True, **kwargs)

    def add_expense(self):
        expense_dict = request.get_json(force=True)
        expense_service = ExpenseServiceImpl(self.db)
        expense_service.add_expense(expense_dict)
        return f"Inseriu {expense_dict} com sucesso!"

    def add_income(self):
        income_dict = request.get_json(force=True)
        income_service = IncomeServiceImpl(self.db)
        income_service.add_income(income_dict)
        return f"Inseriu {income_dict} com sucesso!"
