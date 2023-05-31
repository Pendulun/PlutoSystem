from __future__ import annotations

import pathlib
from typing import Any, Callable, Dict

import dash  # type: ignore
from flask import Flask, make_response, redirect, request
from werkzeug.utils import secure_filename

from pluto._internal.adapters.expense_service import ExpenseServiceImpl
from pluto._internal.adapters.income_service import IncomeServiceImpl
from pluto._internal.adapters.user_service import UserServiceImpl
from pluto._internal.config.config import Config
from pluto._internal.domain.ports.database import Database
from pluto._internal.log import log
from pluto._internal.server.server import Server
from pluto._internal.server.utils import dump_resp

logger = log.logger()


# Based on:
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-5cb
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-part-2-4507
def make_flask_server(config: Config, database: Database) -> Server:
    flask_app = Flask("pluto")

    @flask_app.after_request
    def enable_cors_all(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    server = FlaskServerWrapper(flask_app, config, database)

    from pluto._internal.dash.expenses.callbacks import \
        register_callbacks as register_callbacks1
    from pluto._internal.dash.expenses.layout import layout as layout1

    register_dashapp(
        flask_app, "Expenses", "dash_expenses", layout1, register_callbacks1
    )

    from pluto._internal.dash.incomes.callbacks import \
        register_callbacks as register_callbacks2
    from pluto._internal.dash.incomes.layout import layout as layout2

    register_dashapp(flask_app, "Incomes", "dash_incomes", layout2, register_callbacks2)

    from pluto._internal.dash.exp_and_inc.callbacks import \
        register_callbacks as register_callbacks3
    from pluto._internal.dash.exp_and_inc.layout import layout as layout3

    register_dashapp(flask_app, "Entries", "dash_entries", layout3, register_callbacks3)

    return server


# Based on: https://github.com/okomarov/dash_on_flask/blob/master/app/__init__.py
# https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b
# https://dash.plotly.com/urls
def register_dashapp(
    flask_app: Flask, title, base_pathname, layout, register_callbacks_fun
):
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    my_dashapp = dash.Dash(
        __name__,
        server=flask_app,
        url_base_pathname=f"/{base_pathname}/",
        meta_tags=[meta_viewport],
    )
    # Push an application context so we can use Flask's 'current_app'
    with flask_app.app_context():
        my_dashapp.title = title
        my_dashapp.layout = layout
        register_callbacks_fun(my_dashapp)


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
        Server.DB_IMP = database
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
        self._add_expense_endpoints()
        self._add_income_endpoints()
        self._add_user_endpoints()

    def _add_expense_endpoints(self):
        self.add_endpoint(
            "/expenses/",
            "list_expenses",
            self.list_expenses,
            methods=["GET"],
        )
        self.add_endpoint(
            "/expenses/", "add_expenses", self.add_expense, methods=["POST"]
        )
        self.add_endpoint(
            "/upload/expenses/",
            "upload_expense_file",
            self.expense_file_upload,
            methods=["POST", "GET"],
        )

    def _add_income_endpoints(self):
        self.add_endpoint(
            "/incomes/",
            "list_income",
            self.list_income,
            methods=["GET"],
        )
        self.add_endpoint("/incomes/", "add_income", self.add_income, methods=["POST"])
        self.add_endpoint(
            "/upload/incomes/",
            "upload_income_file",
            self.income_file_upload,
            methods=["POST", "GET"],
        )

    def _add_user_endpoints(self):
        self.add_endpoint(
            "/users/",
            "get_user",
            self.get_user,
            methods=["GET"],
        )
        self.add_endpoint(
            "/users/",
            "add_user",
            self.add_user,
            methods=["POST"],
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

    def list_expenses(self) -> Dict[Any, Any]:
        filters: Dict[str, Any] = request.get_json(force=True)
        expense_service = ExpenseServiceImpl(Server.DB_IMP)
        return dump_resp(expense_service.list_expense(filters))

    def add_expense(self):
        incoming_dict = request.get_json(force=True)
        tag = incoming_dict['tag_name'] if 'tag_name' in incoming_dict else None
        expense_dict = dict(incoming_dict)

        if tag != None:
            del expense_dict['tag_name']

        expense_service = ExpenseServiceImpl(Server.DB_IMP)
        exp_id = expense_service.add_expense_from_dict_without_id(expense_dict)
        if tag != None:
            expense_service.add_tag_for_expense(tag, exp_id)

        return dump_resp()

    def expense_file_upload(self):
        if request.method != "POST":
            # if GET or dont pass any needed condition
            return redirect(request.url)

        fpath = self._upload_file_from_request()

        expense_service = ExpenseServiceImpl(Server.DB_IMP)
        try:
            expense_service.add_expense_from_file(
                file_path=fpath, user_id=request.form["user_id"]
            )
        except Exception as e:
            logger.error(f"Unable to add expense: {e}")
        finally:
            return redirect(request.url)

    def list_income(self):
        args = request.args
        user_id = args["user_id"]
        filter_dict = {"user_id": user_id}
        income_service = IncomeServiceImpl(Server.DB_IMP)
        return dump_resp(income_service.list_income(filter_dict))

    def add_income(self):
        income_dict = request.get_json(force=True)
        income_service = IncomeServiceImpl(Server.DB_IMP)
        income_service.add_income(income_dict)
        return dump_resp()

    def income_file_upload(self):
        if request.method != "POST":
            # if GET or dont pass any needed condition
            return redirect(request.url)

        fpath = self._upload_file_from_request()

        income_service = IncomeServiceImpl(Server.DB_IMP)
        try:
            income_service.add_income_from_file(
                file_path=fpath, user_id=request.form["user_id"]
            )
        except Exception as e:
            logger.error(f"Unable to add income: {e}")
        finally:
            return redirect(request.url)

    def get_user(self):
        args = request.args
        email = args["email"]
        user_service = UserServiceImpl(Server.DB_IMP)
        return dump_resp(user_service.get_user(email))

    def add_user(self):
        user_dict = request.get_json(force=True)
        user_service = UserServiceImpl(Server.DB_IMP)
        user_service.add_user(user_dict)
        return dump_resp()

    # Based on: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
    def _upload_file_from_request(self):
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

            expense_service = ExpenseServiceImpl(Server.DB_IMP)
            try:
                expense_service.add_expense_from_file(
                    file_path=complete_file_path, user_id=request.form["user_id"]
                )
            except Exception:
                # it wasnt possible to add expense
                pass
            finally:
                return redirect(request.url)

        # if GET or dont pass any needed condition
        return redirect(request.url)

    def _allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in self.app.config["ALLOWED_EXTENSIONS"]
        )
