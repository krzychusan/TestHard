from common.utils import log

from threading import Thread
from pyftpdlib import ftpserver
import os

#Function used to ignore ftp server output
def logger(msg):
	pass

class ftpServer(Thread):
	def __init__(self, path, port):
		Thread.__init__(self)
		self.port = port
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
		
                #log('FTP launched on port '+str(self.port)+'.')
                self.ftp.serve_forever()
	
	def close(self):
		#log('Zamykam FTP')
		self.ftp.close_all()


#test = ftpServer()
#test.start()
#test.close()
