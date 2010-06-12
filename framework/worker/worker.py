import socket
import struct
import ftpClient
from common.datapakiet_pb2 import pakiet
from common.bufor import bufor

class worker:
	def __init__(self):
		#CONFIG
		self.host = 'localhost'
		self.port = 11111
		self.path = './ssvn'
		#END

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
				self.ftp.download((self.data.msg, self.data.port), self.path)
				self.data = pakiet()
				self.data.typ = pakiet.FTPDOWNLOAD
				self.data.msg = 'ok'
				self.buffer.send(self.data)
			elif self.data.typ == pakiet.EXIT:
				self.active = False

		self.close()

	def close(self):
		print 'Robota skonczona'
		self.conn.close()
		self.socket.close()

