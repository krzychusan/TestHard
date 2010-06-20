import os

from serwer.IRepository import IRepository
import pysvn

class svn(IRepository):
    def __init__(self):
        self.name = ''
        self.url = ''
        self.Auth = False
        self.login = ''
        self.password = ''
        self.typ = 'svn'
        self.comment = ''
        self.client = pysvn.Client()

    #funkcja pobiera repozytorium svn z adresu repo do folderu dest
    def download(self, repo, dest):
        os.system('find %s -exec rm -rf {} \;' % dest)
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
        
