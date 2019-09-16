# -*- coding: utf-8 -*-
import time
import logging


class Logging:
    def __init__(self):
        logging.basicConfig(filename='logs/app.log', level=logging.INFO)
        logging.basicConfig(filename='logs/fatal.log', level=logging.FATAL)
        logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)
        self.except_hook()
        super(Logging, self).__init__()

    @staticmethod
    def except_hook(exc_type='', exc_value='', traceback=''):
        logging.error("Uncaught exception", exc_info=(exc_type, exc_value, traceback))

    @staticmethod
    def add_time(array):
        new_list = list(array)
        new_list.insert(0, time.asctime())
        return tuple(new_list)

    @staticmethod
    def log(*log_value):
        logging.basicConfig(filename='logs/app.log', level=logging.INFO)
        log_value = Logging.add_time(log_value)
        logging.info(log_value)

    @staticmethod
    def info(*log_value):
        logging.basicConfig(filename='logs/info.log', level=logging.INFO)
        log_value = Logging.add_time(log_value)
        logging.info(log_value)

    @staticmethod
    def exception(*log_value):
        logging.basicConfig(filename='logs/error.log', level=logging.ERROR)
        log_value = Logging.add_time(log_value)
        logging.exception(log_value)

    @staticmethod
    def debug(*log_value):
        logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)
        log_value = Logging.add_time(log_value)
        logging.debug(log_value)

    @staticmethod
    def fatal(*log_value):
        logging.basicConfig(filename='logs/fatal.log', level=logging.FATAL)
        log_value = Logging.add_time(log_value)
        logging.fatal(log_value)
