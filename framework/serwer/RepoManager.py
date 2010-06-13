from serwer.IRepository import IRepository

from common.utils import log
from copy import deepcopy
import common.dbutils as db
import os
import re

#Load plugins to work with differend types of repositories
lista = '/'+'/'.join(os.path.abspath(__file__).split('/')[1:-1])+'/plugins/'
log('Loading repository plugins from '+ lista)
for filename in os.listdir(lista):
    if re.match('rep_.+\.py$',filename):
        log('* '+filename)
        __import__('serwer.plugins.'+filename[:-3])


#Class used to communicate with system which stores data
#about repositories defined by user
class RepoManager:
    repTypes = IRepository.__subclasses__() 
    repList = []

    def convertRepository(self, toConvert):
        for rep in RepoManager.repTypes:
            if (rep().typ == toConvert.typ):
                converted = rep() 
                converted.assign(toConvert.name, toConvert.url, toConvert.comment, toConvert.typ)
                if toConvert.Auth:
                    converted.setAuth(toConvert.login, toConvert.password)
            return converted
        return None

    def addRepository(self, rep):
        db.addRepository(rep.getValuesTuple())
        RepoManager.repList.append(rep)

    def getRepositories(self):
        ls = []
        for a in db.getRepositories():
            ls.append(self.convertRepository(a))
        return ls

    def getRepositoriesTypes(self):
        return RepoManager.repTypes
    
    def getRepository(self, nazwa):
        pass
