# -*- coding: utf-8 -*-


import abc

from core.helpers.rea_math import ReaMath
from core.helpers.transformer import Transformer
from core.helpers.validator import Validator
from core.utilities.json_server import JsonServer
from core.utilities.rest_server import RestServer


class ReaPy(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def validator():
        return Validator()

    def tcp_server(self):
        JsonServer.master = self
        return JsonServer

    def rest_server(self):
        RestServer.master = self
        return RestServer

    @staticmethod
    def rea_math():
        return ReaMath()

    @staticmethod
    def transformer():
        return Transformer()
