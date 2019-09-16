from .string_socket import StringSocket
from core.utilities.logger import Logger


class StringSocketServer(StringSocket):
    def __init__(self, address='127.0.0.1', port=5489):
        super(StringSocketServer, self).__init__(address, port)
        self._bind()

    def _bind(self):
        self.socket.bind((self.address, self.port))

    def _listen(self):
        self.socket.listen(1)

    def _accept(self):
        return self.socket.accept()

    def accept_connection(self):
        self.conn, addr = self._accept()
        Logger.debug("connection accepted, conn socket (%s,%d)" % (addr[0], addr[1]))
        return self.conn, addr

    def _is_connected(self):
        return True if not self.conn else False

    connected = property(_is_connected, doc="True if server is connected")