# -*- coding: utf-8 -*-
from typing import Any, Union
from helpers.validator import Validator


class ReaMath:

    @staticmethod
    def summation(first_number, second_number):
        if Validator.number_control([first_number, second_number]):
            return first_number + second_number
        else:
            return False

    @staticmethod
    def summation_list(number_list):
        total = 0
        if Validator.number_control(number_list):
            for number in number_list:
                total += number
            return total

    @staticmethod
    def extraction(first_number, second_number):
        if Validator.number_control([first_number, second_number]):
            if first_number < second_number:
                return second_number - first_number
            else:
                return first_number - second_number
        else:
            return False

    @staticmethod
    def multiplication(multiplicand, multiplier):
        if Validator.number_control([multiplicand, multiplier]):
            return multiplicand * multiplier
        else:
            return False

    @staticmethod
    def multiplication_list(multiplier_list):
        multiply = 1
        if Validator.number_control(multiplier_list):
            for number in multiplier_list:
                multiply *= number
            return multiply
        else:
            return False

    @staticmethod
    def division(divided, divisor):
        if Validator.number_control([divided, divisor]):
            if divided != 0 and divisor != 0:
                if divided > divisor:
                    return divided / divisor
                else:
                    return divisor / divided
            else:
                return False
        else:
            return False

    @staticmethod
    def division_floor(divided, divisor):
        if Validator.number_control([divided, divisor]):
            if divided != 0 and divisor != 0:
                if divided > divisor:
                    return divided // divisor
                else:
                    return divisor // divided
            else:
                return False
        else:
            return False

    @staticmethod
    def remainder(first_number, second_number):
        if Validator.number_control([first_number, second_number]):
            return first_number % second_number
        else:
            return False

    @staticmethod
    def percent(number, ratio):
        if Validator.number_control([number, ratio]):
            return (number * ratio) / 100
        else:
            return False

    @staticmethod
    def different_percent(first_number, second_number, boolean):
        if Validator.number_control([first_number, second_number]):
            if boolean:
                if first_number < second_number:
                    return (first_number / second_number) * 100
                else:
                    return (second_number / first_number) * 100
            else:
                if first_number > second_number:
                    return (first_number / second_number) * 100
                else:
                    return (second_number / first_number) * 100
        else:
            return False

    @staticmethod
    def exponentiation(number, exponent):
        if Validator.number_control([number, exponent]):
            return number ** exponent
        else:
            return False

    @staticmethod
    def rea_abs(number):
        if Validator.number_control([number]):
            if number > 0:
                return number
            else:
                return -number
        else:
            return False

    @staticmethod
    def rea_sqrt(number, expo, boolean):
        if Validator.number_control([number, expo]):
            if number > 0 and expo >= 0:
                sqrt_number: Union[float, Any] = number ** (1 / expo)
                for i in range(1, 100):
                    if i >= sqrt_number:
                        number = i
                        break
                if boolean:
                    return number
                else:
                    return sqrt_number
            else:
                return False
        else:
            return False

    @staticmethod
    def average(number_list):
        if Validator.number_control(number_list):
            return ReaMath.summation_list(number_list) / len(number_list)
        else:
            return False
