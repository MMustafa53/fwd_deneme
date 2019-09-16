# -*- coding: utf-8 -*-

import os
import json


class Configuration:

    @staticmethod
    def get_configuration():
        path = os.path.dirname(os.path.abspath(__file__)) + "/../../conf/conf.json"
        json_data = json.loads(open(path).read())
        __dict__ = json_data[json_data['env']]
        return __dict__
