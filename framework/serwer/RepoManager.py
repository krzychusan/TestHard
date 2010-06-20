from serwer.IRepository import IRepository

from parsers.base_parser import BaseParser
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
                converted.setTestAttributes(toConvert.build_cmd, toConvert.find_tests_cmd, 
                        toConvert.run_test_cmd)
                converted.compileOnServer = toConvert.compileOnServer
            return converted
        return None

    def addRepository(self, rep):
        db.addRepository(rep.getValuesTuple())

    def getRepositories(self):
        return [self.convertRepository(a) for a in db.getRepositories()]

    def getRepositoriesTypes(self):
        return RepoManager.repTypes
    
    def getRepository(self, nazwa):
        return self.convertRepository(db.getRepositoryByName(nazwa)[0])

    def updateRepository(self, repo, oldName):
        return db.updateRepository(oldName, repo.getValuesTuple())

    def removeRepository(self, nazwa):
        db.removeRepository(nazwa)

    def addResult(self, task_name, result):
        db.addResult((db.taskId(task_name), result.failures, 
            result.errors, result.tests_count, result.log, result.time_elapsed, result.test_case_name))

