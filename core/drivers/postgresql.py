# -*- coding: utf-8 -*-


import psycopg2

from core.utilities.configurator import Configuration


class PgSql:
    connection = None

    def __init__(self):
        super(PgSql).__init__()

    @staticmethod
    def connect():
        try:
            if PgSql.connection is None:
                configurations = Configuration.get_configuration()['system']['tcp_server']['pg_sql']
                PgSql.connection = psycopg2.connect(user=configurations['user'],
                                                    password=configurations['password'],
                                                    host=configurations['host'],
                                                    port=configurations['port'],
                                                    database=configurations['database'])

            return PgSql.connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return False



database=PgSql.connect()
