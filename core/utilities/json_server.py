# -*- coding: utf-8 -*-

from core.utilities.tcp.json.threaded_server import ServerFactoryThread
from core.utilities.tcp.json.threaded_server import ServerFactory
from core.utilities.tcp.json.json_socket import JsonSocket


class JsonServer(ServerFactoryThread):
    master = None

    @staticmethod
    def start_server(address, port, timeout):
        JsonSocket.timeout = timeout
        JsonSocket.port = port
        JsonSocket.address = address
        server = ServerFactory(JsonServer)
        server.start()

    def _process_message(self, obj):
        JsonServer.master.incoming_message(obj)

