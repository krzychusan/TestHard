#!/usr/bin/python
import time
import ConfigParser
import threading
import sys

# TODO: delete imports below
from IRepository import IRepository
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
from RepoManager import *

import RepoManager
import ftpServer
import serverworker
from common.utils import log




class server:
    def __init__(self, repository):
        self.serverCond = threading.Condition()
        self.workersLock = threading.Lock()
        self.workersDone = 0
    
        #Parsowanie konfiguracji serwera
        config = ConfigParser.RawConfigParser()
        config.read('./config.txt')

        self.workersFile = config.get('Worker', 'list')     #lista serverow
        self.workerPort = config.getint('Worker', 'port')       #port na ktorym nasluchuja workerzy
        self.path = config.get('Rep', 'path')       #tymczasowy katalog na dysku dla repozytorium
        self.repository = repository.name       #adres repozytorium
        self.svnauth = repository.auth      #czy wymagana autoryzacja do svna
        self.build_cmd = repository.build_cmd
        self.find_tests_cmd = repository.find_tests_cmd
        self.run_test_cmd = repository.run_test_cmd
        #self.svndownload = config.getboolean('Rep', 'download')        #czy pobierac rep. (moze jest juz)
        self.svndownload = True
        if self.svnauth:
            self.authLogin = repository.login #dane do autoryzacji do svna
            self.authPassword = repository.password

            rep = RepoManager.RepoManager()
            rep = rep.getRepositoriesTypes()[0]
        self.svn = rep()
        if self.svnauth:
            self.svn.setLogin(self.authLogin, self.authPassword)
            self.ftp = ftpServer.ftpServer(self.path, 2222)

    def _find_tests(self):
        cwd = os.getcwd()
        os.chdir(self.path)
        script_cmds = self.find_tests_cmd.split('\n')
        for cmd in script_cmds:
            r = os.system('%s >> output.tmp 2>> output.tmp' % cmd)
            if r != 0:
                print 'Error while running tests'
                break

        f = open('output.tmp', 'r')
        if not f:
            log('Nie mozna otworzyc pliku wyjsciowego')
            f.close()
        lines = f.readlines()
        f.close()
        os.system('rm output.tmp')
        os.chdir(cwd)
        return [self.run_test_cmd.replace('$$', l.rstrip('\n')) for l in lines]


    def _compile(self):
        cwd = os.getcwd()
        os.chdir(self.path)
        script_cmds = self.build_cmd.split('\n')
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
        os.system('rm output.tmp')
        os.chdir(cwd)
        print result


    def start(self):
        if self.svndownload:
            log('Pobieram svn...')
            #self.svn.download(self.repository, self.path)
            log('Svn pobrany.')
        else:
            log('Bez pobierania svn.')

        self._compile()
        self.jobs = self._find_tests()
        self.workers = []
        tmpworker = None
        self.workersLock.acquire()
        self.serverCond.acquire()
        with open(self.workersFile) as f:
            for line in f:
                tmpworker = serverworker.serverworker(line, self.workerPort, self)
                if tmpworker.init():
                    self.workers.append(tmpworker)
                    log('Worker '+line[:-1])
                    tmpworker.start()
        
        self.workersDone = len(self.workers)
        self.workersLock.release()

        if len(self.workers) == 0:
            log('Brak workerow do testowania.')
            return
        
        self.ftp.start()
        self.serverCond.wait()
        self.serverCond.release()
        log('Testy zakonczone.')
        self.ftp.close()
        self.close()

    
    def close(self):
        log('Koniec.')



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        rep = IRepository()
        rep.name = 'http://testhard.unfuddle.com/svn/testhard_project1/' #adres repozytorium
        rep.svnauth = True #czy wymagana autoryzacja do svna
        #rep.find_tests_cmd = 'for i in `seq 1 100`; do echo $i; done'
        rep.find_tests_cmd = 'find . -iname "*test*class"'
        rep.run_test_cmd = 'echo "[junit] Tests run: 1, Failures: 1, Errors: 1, Time elapsed: 1.1 sec $$"'
        rep.auth = True
        rep.build_cmd = 'ant compile'
        rep.authLogin = 'krzychusan' #dane do autoryzacji do svna
        rep.authPassword = '5120045'
    else:
        repo_name = sys.argv[1]
        manager = RepoManager()
        raw_rep = manager.getRepository(repo_name)
        if not raw_rep:
            print 'Nie ma repozytorium o podanej nazwie.'
            sys.exit(-1)
        rep = manager.convertRepository(raw_rep)
    s = server(rep)
    s.start()

