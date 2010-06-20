import ftplib
import os

import sys
import traceback

class ftpClient:
	def __init__(self, myip):
		self.myip = myip
		self.ftp = ftplib.FTP()

	def download(self, url, path):
                print 'url + path:', url, path
                self.done = False
                self.retry = 5
                while not self.done and self.retry > 0:
                    try:
		    	print 'Connecting to ftp'
                        self.ftp.connect(url[0], int(url[1]))
			self.ftp.login('anonymous', self.myip)
			if not os.path.exists(path):
				os.makedirs(path)
                        print 'Downloading ftp ...'
                        try:
			    self.downloadDir('.', path)	
                        except:
                            return False
                        self.done = True
		    except:
                        print 'Failed to connect to ftp'
			#print self.formatExceptionInfo()
                        self.retry -= 1
                
		self.close()
                return True
	
	def downloadDir(self, path, localPath):
		#print 'downloadDir:'+path
		data = []
		self.ftp.dir(path, data.append)
		#print 'LIST', data
		for line in data:
			l = line.split()
			dir = path+'/'+l[8]
			localDir = localPath+'/'+l[8]
			#print 'line: ', line
			if 'd' in l[0]:		#folder
				if l[8][0] == '.':
					continue
				#print 'rekursja: ', dir
				if not os.path.exists(localDir):
				    os.makedirs(localDir)
				self.downloadDir(dir, localDir)
			else:
				#print 'plik: ', dir
				with open(localDir, 'w') as f:
					self.ftp.retrbinary("RETR " + dir, f.write)

	def close(self):
		self.ftp.quit()
                print 'Zamykam FTP'

	def formatExceptionInfo(maxTBlevel=20):
         cla, exc, trbk = sys.exc_info()
         excName = cla.__name__
         try:
             excArgs = exc.__dict__["args"]
         except KeyError:
             excArgs = "<no args>"
         excTb = traceback.format_tb(trbk, maxTBlevel)
         return (excName, excArgs, excTb)

