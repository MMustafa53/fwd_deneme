import socket
import struct
from core import Logger


class StringSocket(object):
    def __init__(self, address='127.0.0.1', port=5489):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = self.socket
        self._address = address
        self._port = port

    def send_obj(self, msg, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn

        if self.socket:
            frmt = "=%ds" % len(msg.encode())
            packed_msg = struct.pack(frmt, msg.encode())
            packed_hdr = struct.pack('!I', len(packed_msg))
            self._send(packed_hdr, con)
            self._send(packed_msg, con)

    def _send(self, msg, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn

        sent = 0
        while sent < len(msg):
            sent += con.send(msg[sent:])

    def _read(self, size, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn


        data = b''
        while len(data) < size:
            data_tmp = con.recv(size - len(data))
            data += data_tmp
            if data_tmp == b'':
                raise RuntimeError("socket connection broken")
        return data

    def _msg_length(self, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn

        d = self._read(4, con)
        s = struct.unpack('!I', d)
        return s[0]

    def read_obj(self, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn

        size = self._msg_length(con)
        data = self._read(size, con)
        frmt = "=%ds" % size
        msg = struct.unpack(frmt, data)
        return msg[0].decode()

    def close(self, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn

        self._close_socket()
        if self.socket is not conn:
            self._close_connection(con)

    def _close_socket(self):
        Logger.debug("closing main socket")
        self.socket.close()

    def _close_connection(self, conn=None):
        con = None
        if conn is not None:
            con = conn
        else:
            con = self.conn

        Logger.debug("closing the connection socket")
        con.close()

    def _get_address(self):
        return self._address

    def _set_address(self, address):
        pass

    def _get_port(self):
        return self._port

    def _set_port(self, port):
        pass

    address = property(_get_address, _set_address, doc='read only property socket address')
    port = property(_get_port, _set_port, doc='read only property socket port')