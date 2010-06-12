import os

#Class used to communicate with system which stores data
#about repositories defined by user
class RepConnector:
    repTypes = []
    repList = []

    def convertRepository(self, toConvert):
        for rep in RepConnector.repTypes:
            if (rep.typ == toConvert.typ):
                converted = copy.deepcopy(rep)
                converted.assign(toConvert.name, toConvert.url, toConvert.comment, toConvert.typ)
                if toConvert.Auth:
                    converted.setAuth(toConvert.login, toConvert.password)
            return converted
        return None

    def addRepository(self, rep):
        RepConnector.repList.append(rep)

    def getRepositories(self):
        return RepConnector.repList

    def getRepositoriesTypes(self):
        return RepConnector.repTypes
    
    def getRepository(self, nazwa):
        for rep in RepConnector.repList:
            if rep.name == nazwa:
                return rep
        

#Abstract class providing interface to create plugins for 
#different version control systems
class Repository:
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

    @staticmethod
    def initialize(obj):
        print 'dodaje svn'
        for con in RepConnector.repTypes:
            if con.typ == 'svn':
                break
        else:
            RepConnector.repTypes.append(obj)


import re
print 'Loading plugins...'
#Load plugins to work with differend types of repositories
for filename in os.listdir(os.getcwd()+'/framework/plugins/'):
    if re.match('rep_.+\.py',filename):
        print filename
        __import__('framework.plugins.'+filename[:-3])


