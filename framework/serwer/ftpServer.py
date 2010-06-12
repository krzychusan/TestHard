from threading import Thread
from pyftpdlib import ftpserver
import os
''' Wymagana jest zainstalowana biblioteka pyftpdlib
	Nalezy pobrac: http://pyftpdlib.googlecode.com/files/pyftpdlib-0.5.2.tar.gz
	Potem 	(linux) sudo python setup.py install
			(windows) setup.py install
'''

def logger(msg):
	pass

class ftpServer(Thread):
	def __init__(self, path):
		Thread.__init__(self)
		self.port = 2222
		self.path = path

	def run(self):
		self.authorize = ftpserver.DummyAuthorizer()
		self.authorize.add_anonymous(os.path.abspath(self.path))

		ftpserver.log = logger
		ftpserver.logline = logger
		ftpserver.logerror = logger

		self.handler = ftpserver.FTPHandler
		self.handler.authorizer = self.authorize
		self.ftp = ftpserver.FTPServer(('127.0.0.1', self.port), self.handler)
		self.ftp.serve_forever()
	
	def close(self):
		self.ftp.close_all()


#test = ftpServer()
#test.start()
#test.close()
