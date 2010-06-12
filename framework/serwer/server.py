import repo.svn
import ftpServer
import serverworker
import time
import ConfigParser
import threading

def log(info):
	print time.strftime('%X %x'),info

class server:
	def __init__(self):
		self.serverCond = threading.Condition()
		self.workersLock = threading.Lock()
		self.workersDone = 0
	
		#Parsowanie konfiguracji serwera
		config = ConfigParser.RawConfigParser()
		config.read('./config.txt')

		self.workersFile = config.get('Worker', 'list')		#lista serverow
		self.workerPort = config.getint('Worker', 'port')		#port na ktorym nasluchuja workerzy
		self.path = config.get('Rep', 'path')		#tymczasowy katalog na dysku dla repozytorium
		self.repository = config.get('Rep', 'url')		#adres repozytorium
		self.svnauth = config.getboolean('Rep', 'auth')		#czy wymagana autoryzacja do svna
		self.svndownload = config.getboolean('Rep', 'download')		#czy pobierac rep. (moze jest juz)
		if self.svnauth:
			self.authLogin = config.get('Rep', 'login')	#dane do autoryzacji do svna
			self.authPassword = config.get('Rep', 'password')

		self.svn = repo.svn.svn()
		if self.svnauth:
			self.svn.setLogin(self.authLogin, self.authPassword)
                self.ftp = ftpServer.ftpServer(self.path)

	def start(self):
		if self.svndownload:
			log('Pobieram svn...')
			self.svn.download(self.repository, self.path)
			log('Svn pobrany.')
		else:
			log('Bez pobierania svn.')

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
		self.ftp.close()
		log('Zamykam FTP')
		self.close()

	
	def close(self):
		log('Koniec')

