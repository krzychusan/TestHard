import serwer.TasksManager as tm
import common.dbutils as db
import time

import subprocess

taskManager = tm.TasksManager()

while True:
    print '.'
    tasks = db.getUnfinishedTasks()
    if len(tasks) > 0:
        print 'Launching task %s.' % tasks[0]['name']
        retcode = subprocess.call(["./run.sh", "run-server", tasks[0]['repository'], tasks[0]['name']])
        print 'Task %s done!' % tasks[0]['name']
    time.sleep(5)
    
