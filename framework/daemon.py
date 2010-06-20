import serwer.RepoManager as rp
import serwer.TasksManager as tm
import common.dbutils as db
import time

repoManager = rp.RepoManager()
taskManager = tm.TasksManager()

while true:
    tasks = db.getUnfinishedTasks()
    if len(tasks) > 0:
        pass
    time.sleep(60)
