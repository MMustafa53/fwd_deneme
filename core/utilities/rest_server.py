# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from core.utilities.rest.resource.HelloWorld import HelloWorld


class RestServer(object):
    master = None

    @staticmethod
    def start_server(address, port, debug=False):
        app = Flask(__name__)
        api = Api(app)

        api.add_resource(HelloWorld, '/')

        app.run(host=address, port=port, debug=debug)
