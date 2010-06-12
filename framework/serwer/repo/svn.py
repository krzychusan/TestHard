import pysvn
from IRepo import IRepo

class svn(IRepo):
	'''	klasa odpowiedzialna za komunikacje z svnem, pobiera repozytorium
		i zapisuje na dysku we wskazanym folderze. Umozliwia takze
		uwierzytelnianie jezeli jest wymagane przez svna. '''

	def __init__(self):
		self.client = pysvn.Client()

	#funkcja pobiera repozytorium svn z adresu repo do folderu dest
	def download(self, repo, dest):	
		self.client.checkout(repo, dest)

	#funkcja ustawia login i haslo dla uzytkownika, jezeli jest 
	#wymagane uwierzytelnianie na svnie
	def setLogin(self, login, password):
		self.login = login
		self.password = password
		self.client.callback_get_login = self._loginCallback
	
	#pomocnicza funkcja wymagana przy logowaniu
	def _loginCallback(self, realm, username, may_save):
		return True, self.login, self.password, True
		

