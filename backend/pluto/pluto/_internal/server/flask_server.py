from __future__ import annotations

import pathlib
from typing import Callable

from flask import Flask, make_response, redirect, request
from werkzeug.utils import secure_filename

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
    FILE_UPLOAD_ALLOWED_EXTENSIONS = {"csv"}
    UPLOAD_FOLDER = "./tmp_files/"

    def __init__(self, app: Flask, config: Config, database: Database):
        super().__init__(config)
        self.app = app
        self.db = database
        self.configs(self._cfg)
        self.app.config["UPLOAD_FOLDER"] = FlaskServerWrapper.UPLOAD_FOLDER
        self.app.config[
            "ALLOWED_EXTENSIONS"
        ] = FlaskServerWrapper.FILE_UPLOAD_ALLOWED_EXTENSIONS

        self._add_endpoints()

    def configs(self, config: Config):
        for config_name, value in config.as_dict().items():
            self.app.config[config_name.upper()] = value

    def _add_endpoints(self):
        self.add_endpoint(
            "/expenses/", "add_expenses", self.add_expense, methods=["POST"]
        )
        self.add_endpoint("/incomes/", "add_income", self.add_income, methods=["POST"])
        self.add_endpoint(
            "/upload/expenses/",
            "upload_expense_file",
            self.expense_file_upload,
            methods=["POST", "GET"],
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
        expense_service.add_expense_from_dict_without_id(expense_dict)
        return f"Inseriu {expense_dict} com sucesso!"

    def add_income(self):
        income_dict = request.get_json(force=True)
        income_service = IncomeServiceImpl(self.db)
        income_service.add_income(income_dict)
        return f"Inseriu {income_dict} com sucesso!"

    # Based on: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
    def expense_file_upload(self):
        base_html_return = """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="/upload/expenses/" method=post enctype=multipart/form-data>
        <input type="hidden" id="user_id" name="user_id" value="3487">
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        """
        if request.method == "POST":
            # check if the post request has the file part
            if "file" not in request.files:
                return redirect(request.url)

            file = request.files["file"]

            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == "":
                return redirect(request.url)

            if file and self._allowed_file(file.filename):
                filename = secure_filename(file.filename)

                upload_folder = pathlib.Path(self.app.config["UPLOAD_FOLDER"])
                upload_folder.mkdir(parents=True, exist_ok=True)

                complete_file_path = upload_folder / filename
                file.save(complete_file_path)

                expense_service = ExpenseServiceImpl(self.db)
                try:
                    expense_service.add_expense_from_file(
                        file_path=complete_file_path, user_id=request.form["user_id"]
                    )
                except Exception as e:
                    return_html = base_html_return + f"\nErro no processamento: {e}"
                    return return_html
                else:
                    return redirect(request.url)

            else:
                return base_html_return + "\n Arquivo inválido!"

        # if GET
        return base_html_return

    def _allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in self.app.config["ALLOWED_EXTENSIONS"]
        )
