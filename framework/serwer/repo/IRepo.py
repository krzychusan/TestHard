
class IRepo:
	#Interfejs odpowiedzialny za komunikacje z
	#serwerem przechowywujacym testowana aplikacje
	
	def download(self, repo, dest):
		pass
	
	def setLogin(self, login, password):
		pass
