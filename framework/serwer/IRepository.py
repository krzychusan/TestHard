
#Abstract class providing interface to create plugins for 
#different version control systems
class IRepository(object):
    def __init__(self):
        self.name = ''
        self.url = ''
        self.Auth = False
        self.login = ''
        self.password = ''
        self.typ = 'Interface'
        self.comment = ''

    def assign(self, name, url, comment, typ):
        self.name = name
        self.url = url
        self.comment = comment
        self.typ = typ

    def download(self, url, revision):
        raise NotImplementedError("Abstract class")

    def setAuth(self, login, password):
        self.Auth = True
        self.login = login
        self.password = password
	
	def getValuesTuple(self):
		return ( self.name, self.url, self.comment \
				self.typ, self.login, self.password )
