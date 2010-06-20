import socket
import struct
import os
import ftpClient
from common.datapakiet_pb2 import pakiet
from common.bufor import bufor

class worker:
    def __init__(self):
        #CONFIG
        self.host = ''
        self.port = 11111
        self.path = './ssvn'
        #END

    def _compile(self):
        cwd = os.getcwd()
        os.chdir(self.path)

        script_cmds = self.data.msg.split('\n')
        for cmd in script_cmds:
            r = [0, 0, 0]
            r[0] = os.system('echo " +++ TESTHARD +++ Running %s:" >> output.tmp' % cmd)
            r[1] = os.system('%s >> output.tmp 2>> output.tmp' % cmd)
            r[2] = os.system('echo " +++ TESTHARD +++ Last command result: %d" >> output.tmp' % r[1])
            if r != [0, 0, 0]:
                print 'Error while running tests'
                break

        f = open('output.tmp', 'r')
        if not f:
            print 'Nie mozna otworzyc pliku wyjsciowego'
            self.close()
        result = ''.join(f.readlines())

        self.data = pakiet()
        self.data.typ = pakiet.BUILD
        self.data.msg = result
        self.buffer.send(self.data)

        os.system('rm output.tmp')
        os.chdir(cwd)

    def _run_test(self):
        cwd = os.getcwd()
        os.chdir(self.path)

        cmd = self.data.msg
        print 'Run', cmd

        retcode = os.system('%s >> output.tmp 2>> output.tmp' % cmd)
        f = open('output.tmp', 'r')
        if not f:
            print 'Nie mozna otworzyc pliku wyjsciowego'
            self.close()
        result = ''.join(f.readlines())

        self.data = pakiet()
        self.data.typ = pakiet.RUNTESTS
        self.data.msg = result
        self.buffer.send(self.data)
        
        os.system('rm output.tmp')
        os.chdir(cwd)

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.active = True
        self.ftp = ftpClient.ftpClient(self.socket.getsockname()[0])
        self.conn, self.addr = self.socket.accept()
        self.buffer = bufor(self.conn)
        
        while self.active:
            self.data = self.buffer.read()
            if not self.data:
                print 'Serwer zakonczyl nieoczekiwanie sesje.'
                break
            if self.data.typ == pakiet.PING and self.data.msg == 'ping':
                self.data = pakiet()
                self.data.typ = pakiet.PING
                self.data.msg = 'pong'
                self.buffer.send(self.data)
            elif self.data.typ == pakiet.FTPDOWNLOAD:
                if not self.ftp.download((self.data.msg, self.data.port), self.path):
                    return
                self.data = pakiet()
                self.data.typ = pakiet.FTPDOWNLOAD
                self.data.msg = 'ok'
                self.buffer.send(self.data)
            elif self.data.typ == pakiet.RUNTESTS:
                self._run_test()
            elif self.data.typ == pakiet.BUILD:
                self._compile()
            elif self.data.typ == pakiet.EXIT:
                self.active = False

        self.close()

    def close(self):
        print 'Robota skonczona'
        self.conn.close()
        self.socket.close()

