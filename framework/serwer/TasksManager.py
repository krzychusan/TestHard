from serwer.IRepository import IRepository

from common.utils import log
import common.dbutils as db

class TasksManager:
    def addTest(self, name, repo, date, email, comment):
        db.addTask((name, date, comment, email, repo))
        return True

    def getTask(self, name):
        return db.getTaskByName(name)

    def getTasks(self):
        return db.getTasks()

    def removeTask(self, name):
        db.removeTask(name)
        return True
