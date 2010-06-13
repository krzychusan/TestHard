from IRepository import IRepository

from common.utils import log
import os
import re

#Load plugins to work with differend types of repositories
lista = '/'+'/'.join(os.path.abspath(__file__).split('/')[1:-1])+'/plugins/'
log('Loading repository plugins from '+ lista)
for filename in os.listdir(lista):
    if re.match('rep_.+\.py$',filename):
        log('* '+filename)
        __import__('framework.plugins.'+filename[:-3])


#Class used to communicate with system which stores data
#about repositories defined by user
class RepoManager:
    repTypes = IRepository.__subclasses__() 
    repList = []

    def convertRepository(self, toConvert):
        for rep in RepoManager.repTypes:
            if (rep.typ == toConvert.typ):
                converted = copy.deepcopy(rep)
                converted.assign(toConvert.name, toConvert.url, toConvert.comment, toConvert.typ)
                if toConvert.Auth:
                    converted.setAuth(toConvert.login, toConvert.password)
            return converted
        return None

    def addRepository(self, rep):
        RepoManager.repList.append(rep)

    def getRepositories(self):
        return RepoManager.repList

    def getRepositoriesTypes(self):
        return RepoManager.repTypes
    
    def getRepository(self, nazwa):
        for rep in RepoManager.repList:
            if rep.name == nazwa:
                return rep

