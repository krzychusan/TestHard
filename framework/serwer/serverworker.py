from threading import Thread
import socket
import server
import struct
from common.datapakiet_pb2 import pakiet
from common.bufor import bufor
from common.utils import log

class serverworker(Thread):

    def __init__(self, ip, port, server):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.server = server
        self.connected = False
        self.ftpDownloaded = False

    def init(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = bufor(self.socket)
        if self.socket.connect_ex((self.ip, self.port)):
            return False
        else:
            return True

    def run(self):
        #Send ping
        self.data = pakiet()
        self.data.typ = pakiet.PING
        self.data.msg = 'ping'
        self.buffer.send(self.data)

        #Recv ping
        self.data = self.buffer.read()
        if self.data.typ != pakiet.PING or self.data.msg != 'pong':
            #wyslij error
            print 'Bledna odpowiedz na ping!'
            self.close()
            return
        
        #pobieranie aplikacji testowanej przez workera
        self.data = pakiet()
        self.data.typ = pakiet.FTPDOWNLOAD
        self.data.port = 2222   # TODO: poprawic!
        self.data.msg = self.socket.getsockname()[0]
        self.buffer.send(self.data)

        self.data = self.buffer.read()
        if self.data.typ != pakiet.FTPDOWNLOAD or self.data.msg != 'ok':
            print 'Worker nie pobral FTP ', self.data.msg
            self.close()
            return
        
        self.ftpDownloaded = True

        self.data = pakiet()
        self.data.typ = pakiet.RUNTESTS
        self.data.msg = 'ls'
        self.buffer.send(self.data)

        self.data = self.buffer.read()
        if not self.data or self.data.typ != pakiet.RUNTESTS:
            print 'Blad podczas wykonywania testow'
            #self.close()
            #return

        print 'Wykonano testy', self.data.msg

        self.server.workersLock.acquire()
        self.server.workersDone -= 1
        if self.server.workersDone == 0:
            self.server.serverCond.acquire()
            self.server.serverCond.notify()
            self.server.serverCond.release()
        self.server.workersLock.release()
        log('Worker '+self.ip[:-1]+' pobral FTP')

        #koniec pracy
        self.data = pakiet()
        self.data.typ = pakiet.EXIT
        self.buffer.send(self.data)
        
        self.close()

    def close(self):
        self.socket.close()
