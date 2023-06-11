from multiprocessing import Process
import os
import signal

import pytest


from pluto._internal.server.flask_server import make_flask_server, FlaskServerWrapper
from tests._internal.mocks import ConfigMock, DatabaseMock
import random
import requests

class ParallelServer(FlaskServerWrapper):
    def __init__(self, srv):
        self.srv = srv
        self.app = srv.app
        self.process = None
        
    def run(self):
        if self.process is not None:
            self.__delete__()
        self.process = Process(target=self.srv.run)
        self.process.start()
            
    def __delete__(self):
        if self.process is None:
            return
        self.process.terminate()
        self.process.join()
        self.process = None

class TestFlaskServer:
    @pytest.fixture
    def server(self):
        srv = make_flask_server(ConfigMock.parse(), DatabaseMock(ConfigMock.parse()))
        return ParallelServer(srv)

    @pytest.fixture
    def client(self):
        srv = make_flask_server(ConfigMock.parse(), DatabaseMock(ConfigMock.parse()))
        with srv.app.test_client() as c:
            yield c

    def test_init(self, server):
        pass

    def test_run_stop(self, server):
        server.run()
        server.__delete__()

    def test_run_stop(self, server):
        server.run()
        server.__delete__()

    def test_upload_file_from_request(self, server):
        class File:
            def __init__(self, filename):
                self.filename = filename

            def save(self, filepath):
                pass

        class Request:
            def __init__(self, filename):
                self.files = dict(file=File(filename))

        server._upload_file_from_request(Request("tests/fixtures/valid_incomes.csv"))

    def test_list_incomes(self, client):
        client.post("/incomes/", data={"user_id": "putin"})
        incomes = client.get("/incomes/")
        print(incomes)

    def test_income_upload(self, client):
        # TODO: Properly test file upload. I found an example at
        # https://stackoverflow.com/questions/35684436/testing-file-uploads-in-flask
        client.post("/upload/incomes/", data={})

    def test_expense_upload(self, client):
        # TODO: properly test file upload
        client.post("/upload/expenses/", data={})

    def test_list_expenses(self, client):
        client.post("/expenses/", data={"user_id": "putin"})
        expenses = client.get("/expenses/")
        print(expenses)

    def test_get_user(self, client):
        client.post("/users/", data={"email": "putin@massacre.death"})
        client.get("/users/", data={"email": "putin@massacre.death"})

