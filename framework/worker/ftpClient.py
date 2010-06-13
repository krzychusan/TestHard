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
                try:
			self.ftp.connect(url[0], int(url[1]))
			self.ftp.login('anonymous', self.myip)
			if not os.path.exists(path):
				os.makedirs(path)
			self.downloadDir('.', path)	
		except:
			print self.formatExceptionInfo()

		self.close()
	
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

	def formatExceptionInfo(maxTBlevel=20):
         cla, exc, trbk = sys.exc_info()
         excName = cla.__name__
         try:
             excArgs = exc.__dict__["args"]
         except KeyError:
             excArgs = "<no args>"
         excTb = traceback.format_tb(trbk, maxTBlevel)
         return (excName, excArgs, excTb)

