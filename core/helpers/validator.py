# -*- coding: utf-8 -*-
import re

from helpers.transformer import Transformer


class Validator:

    @staticmethod
    def type_control(types, value):

        if types == 'ip':
            ip_pattern = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", value)
            if ip_pattern:
                return True
            else:
                return False
        else:
            return False

    # noinspection PyTypeChecker
    @staticmethod
    def number_control(listed):
        i = 0
        while i < len(listed):
            if isinstance(listed[i], (float, int)):
                return True
            else:
                try:
                    listed[i] = Transformer.ohb_to_all(listed[i], float)
                    return True
                except ValueError or TypeError:
                    print(ValueError, TypeError)
                    return False
