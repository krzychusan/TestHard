from datapakiet_pb2 import pakiet
import struct

class bufor:
    def __init__(self, sock):
        self.socket = sock

def _recv(self, size):
        b = ""
        left = size
        while left > 0:
        tmp = self.socket.recv(left)
        left -= len(tmp)
        b += tmp 
        return b

    def read(self):
        self.size = self.socket.recv(2)
        if not self.size:
            return
        self.dataSize = struct.unpack("H", self.size)[0]
        self.data = self._recv(self.dataSize)
        self.ret = pakiet()
        self.ret.ParseFromString(self.data)
        return self.ret

    def send(self, msg):
        self.msg = msg.SerializeToString()
        self.socket.send(struct.pack("H", len(self.msg)))
        self.socket.send(self.msg)

