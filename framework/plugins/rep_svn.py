from ..repository import Repository

class svn(Repository):
    def __init__(self):
        self.name = ''
        self.url = ''
        self.Auth = False
        self.login = ''
        self.password = ''
        self.typ = 'svn'
        self.comment = ''

    def download(self, url, revision):
        pass

    def setAuth(self, login, password):
        pass

svn.initialize(svn())
