import threading
from core.utilities.tcp.string.string_socket_server import StringSocketServer
from core.utilities.logger import Logger
import socket
from core.utilities.tcp_response import TcpResponse


class ThreadedStringServer(threading.Thread, StringSocketServer):
    def __init__(self, address='127.0.0.1', port=5489):
        threading.Thread.__init__(self)
        StringSocketServer.__init__(self, address=address, port=port)
        self._isAlive = False
        self._listen()

    def _processMessage(self, obj, conn):
        """ virtual method """
        pass

    def _first_connection(self, obj, conn):
        """ virtual method """
        pass

    def run(self):
        while self._isAlive:
            try:
                conn, addr = self.accept_connection()
                TcpResponse(self, conn, addr).start()
            except socket.timeout as e:
                Logger.debug("socket.timeout: %s" % e)
                continue
            except Exception as e:
                Logger.exception(e)
                continue

    def start(self):
        self._isAlive = True
        super(ThreadedStringServer, self).start()

    def stop(self):
        """ The life of the dead is in the memory of the living """
        self._isAlive = False