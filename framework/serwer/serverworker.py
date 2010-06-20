from threading import Thread
import socket
import server
import struct
from common.datapakiet_pb2 import pakiet
from common.bufor import bufor
from common.utils import log

import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
from RepoManager import *

from parsers.ant_junit import AntJUnitParser

class serverworker(Thread):

    def __init__(self, ip, port, server):
        Thread.__init__(self)
        self.ip = ip.rstrip('\n')
        self.port = port
        self.server = server
        self.connected = False
        self.ftpDownloaded = False

    def init(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = bufor(self.socket)
        #import pdb; pdb.set_trace()
        if self.socket.connect_ex((self.ip, self.port)):
            return False
        else:
            return True

    def _test(self, test_cmd):
        self.data = pakiet()
        self.data.typ = pakiet.RUNTESTS
        self.data.msg = test_cmd
        self.buffer.send(self.data)

        self.data = self.buffer.read()
        if self.data.typ != pakiet.RUNTESTS:
            print 'Blad w wykonywaniu testow!', self.data.msg
            self.close()
            return
 
        print 'RETURNED', self.data.msg
        results = AntJUnitParser(self.data.msg)
        return results

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
        log('Worker '+self.ip[:-1]+' pobral FTP')

        self.data = pakiet()
        self.data.typ = pakiet.BUILD
        self.data.msg = 'ant compile'
        self.buffer.send(self.data)

        self.data = self.buffer.read()
        if not self.data or self.data.typ != pakiet.BUILD:
            log('Blad podczas budowania')
            #self.close()
            #return
    
        rep = RepoManager()

        while True:
            self.server.workersLock.acquire()
            if len(self.server.jobs) > 0:
                job = self.server.jobs[0]
                self.server.jobs = self.server.jobs[1:]
            else:
                self.server.workersLock.release()
                self.server.serverCond.acquire()
                self.server.serverCond.notify()
                self.server.serverCond.release()
                break
            self.server.workersLock.release()

            results = self._test(job)
            rep = RepoManager()
            rep.addResult(self.server.taskName, results)
            print 'WYNIKI TESTOW'
            print 'ILE: %d FAILURES: %d, ERRORS: %d LOG:' % (results.tests_count, results.failures, results.errors)
            print '/-------------\\'
            print results.log
            print '\\-------------/'


        #koniec pracy
        self.data = pakiet()
        self.data.typ = pakiet.EXIT
        self.buffer.send(self.data)
        
        self.close()

    def close(self):
        self.socket.close()
