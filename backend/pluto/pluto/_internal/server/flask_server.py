from __future__ import annotations

from flask import Flask, request, make_response

from pluto._internal.config.config import Config
from pluto._internal.server.server import Server

from typing import Callable


#Based on:
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-5cb
# https://dev.to/nandamtejas/implementing-flask-application-using-object-oriented-programming-oops-part-2-4507
def make_flask_server(config: Config) -> Server:
    flask_app = Flask(__name__)
    server = FlaskServerWrapper(flask_app, config)
    server.add_endpoint('/action/<string:name>', 'action', action)
    return server

def action(name):
    """
    This function takes `name` argument and returns `Hello <name>`.
    """
    return "Hello " + name

class EndpointHandler(object):

    def __init__(self, action):
        self.action = action 

    def __call__(self, *args, **kwargs):
        response = self.action(*args, **request.view_args)
        return make_response(response)

class FlaskServerWrapper(Server):

    def __init__(self, app:Flask, config:Config):
        self.app = app
        self.configs(config)

    def configs(self, config:Config):
        for config, value in config.as_dict().items():
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint:str=None, endpoint_name:str=None, handler:Callable=None, methods:list=None, *args, **kwargs):
        if methods is None:
            methods = ['GET']
        
        self.app.add_url_rule(endpoint, endpoint_name, EndpointHandler(handler), methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(debug=True, **kwargs)