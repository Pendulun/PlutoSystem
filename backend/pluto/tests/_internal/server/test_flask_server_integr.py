from multiprocessing import Process
import pytest
import pathlib

from pluto._internal.server.flask_server import make_flask_server, FlaskServerWrapper
from tests._internal.mocks import ConfigMock, DatabaseMock

from werkzeug.datastructures import FileStorage
from flask.testing import FlaskClient

test_files_path = pathlib.Path(__file__).parent / "test_files"


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
    def client(self) -> FlaskClient:
        srv = make_flask_server(ConfigMock.parse(), DatabaseMock(ConfigMock.parse()))
        # Based on https://flask.palletsprojects.com/en/2.3.x/testing/
        srv.app.config.update({"TESTING":True})
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

    def test_list_incomes(self, client:FlaskClient):
        incomes = client.get("/incomes/", query_string={"user_id": "putin"})
        print(incomes)

    def test_valid_income_upload(self, client:FlaskClient):
        # Based on
        # https://stackoverflow.com/questions/35684436/testing-file-uploads-in-flask
        my_file = FileStorage(
            stream=open(test_files_path / "test_incomes1.csv", "rb"),
            filename="test_incomes1.csv",
            content_type="text/csv",
        )

        data = dict()
        data['file'] = my_file
        data['user_id'] = "daniel"
        response = client.post("/upload/incomes/", data=data)
        assert b"Arquivo processado com sucesso!" in response.data
    
    def test_invalid_income_upload(self, client:FlaskClient):
        # Based on
        # https://stackoverflow.com/questions/35684436/testing-file-uploads-in-flask
        my_file = FileStorage(
            stream=open(test_files_path / "test_incomes2.csv", "rb"),
            filename="test_incomes2.csv",
            content_type="text/csv",
        )

        data = dict()
        data['file'] = my_file
        data['user_id'] = "daniel"
        response = client.post("/upload/incomes/", data=data)
        assert b"Erro ao processar o arquivo!" in response.data

    def test_valid_expense_upload(self, client:FlaskClient):
        my_file = FileStorage(
            stream=open(test_files_path / "test_expenses1.csv", "rb"),
            filename="test_expenses1.csv",
            content_type="text/csv",
        )
        
        data = dict()
        data['file'] = my_file
        data['user_id'] = "daniel"
        response = client.post("/upload/expenses/", data=data)
        assert b"Arquivo processado com sucesso!" in response.data

    def test_invalid_expense_upload(self, client:FlaskClient):
        my_file = FileStorage(
            stream=open(test_files_path / "test_expenses2.csv", "rb"),
            filename="test_expenses2.csv",
            content_type="text/csv",
        )
        
        data = dict()
        data['file'] = my_file
        data['user_id'] = "daniel"
        response = client.post("/upload/expenses/", data=data)
        assert b"Erro ao processar o arquivo!" in response.data

    def test_list_expenses(self, client:FlaskClient):
        client.post("/expenses/", data={"user_id": "putin"})
        response = client.get("/expenses/")
        print(response.data)

    def test_get_user(self, client:FlaskClient):
        new_user = {"email": "putin@ru.com","name":"putin","password":"123"}
        response = client.post("/users/", json=new_user)
        assert b"Usuario adicionado com sucesso!" in response.data
        response = client.get("/users/", query_string={"email": "putin@ru.com"})
        # Já que não temos conexão real com o bd
        assert b'null' in response.data
    
    def test_add_invalid_user(self, client:FlaskClient):
        #Faltam informações de email e password para o usuário
        new_user = {"email": "putin@ru.com"}
        response = client.post("/users/", json=new_user)
        assert b"Erro ao adicionar usuario!" in response.data
    
    def test_add_valid_expense_without_tag(self, client:FlaskClient):
        new_expense = {"user_id":"daniel", "src":"EPA", "amount":20}
        response = client.post("/expenses/", json=new_expense)
        assert b"Despesa adicionada com sucesso!" in response.data

    def test_add_valid_expense_with_tag(self, client:FlaskClient):
        new_expense = {"user_id":"daniel", "src":"EPA", "amount":20, "tag_name":"Mercado"}
        response = client.post("/expenses/", json=new_expense)
        assert b"Despesa adicionada com sucesso!" in response.data
    
    def test_add_invalid_expense_without_tag(self, client:FlaskClient):
        # Falta a informação de src
        new_expense = {"user_id":"daniel", "amount":20}
        response = client.post("/expenses/", json=new_expense)
        assert b"Erro ao adicionar despesa!" in response.data
    
    def test_add_expense_invalid_amount_without_tag(self, client:FlaskClient):
        new_expense = {"user_id":"daniel", "src":"Araujo", "amount":"aaa"}
        response = client.post("/expenses/", json=new_expense)
        assert b"Erro ao adicionar despesa!" in response.data
    
    def test_add_valid_expense_with_invalid_tag(self, client:FlaskClient):
        new_expense = {"user_id":"daniel", "src":"EPA", "amount":20, "tag_name":None}
        response = client.post("/expenses/", json=new_expense)
        assert b"Despesa adicionada com sucesso!" in response.data
    
    def test_add_valid_expense_with_tag_with_spaces(self, client:FlaskClient):
        new_expense = {"user_id":"daniel", "src":"EPA", "amount":20, "tag_name":" Mercado "}
        response = client.post("/expenses/", json=new_expense)
        assert b"Despesa adicionada com sucesso!" in response.data
    
    def test_add_valid_income(self, client:FlaskClient):
        new_income = {"user_id":"daniel", "src":"Salario", "amount":1000}
        response = client.post("/incomes/", json=new_income)
        assert b"Receita adicionada com sucesso!" in response.data
    
    def test_add_income_invalid_amount(self, client:FlaskClient):
        new_income = {"user_id":"daniel", "src":"Salario", "amount": "aaa"}
        response = client.post("/incomes/", json=new_income)
        assert b"Erro ao adicionar receita!" in response.data
    
    def test_add_income_missing_info(self, client:FlaskClient):
        # Falta a informação de src
        new_income = {"user_id":"daniel", "amount": "aaa"}
        response = client.post("/incomes/", json=new_income)
        assert b"Erro ao adicionar receita!" in response.data