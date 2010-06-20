import serwer.TasksManager as tm
import common.dbutils as db
import time
import common.mailSender as ms
import subprocess
import os

taskManager = tm.TasksManager()

while True:
    print '.'
    tasks = db.getUnfinishedTasks()
    if len(tasks) > 0:
        print 'Launching task %s.' % tasks[0]['name']
        retcode = os.system("./run.sh %s %s %s >> log.txt 2>> log.txt" % ("run-server", tasks[0]['repository'], tasks[0]['name']))
        currentTask = db.getTaskByName(tasks[0]['name'])
        if currentTask['errors_count'] is not None:
            content = 'Zadanie ' + currentTask['name'] + ' zostalo zakonczone.\n' + \
                  'Failures: ' + str(currentTask['failures_count']) + '\n' + \
                  'Errors: ' + str(currentTask['errors_count']) + '\n' + \
                  'Total tests count: ' + str(currentTask['tests_count']) + '\n' + \
                  'Szczegolowy opis wynikow zadania w dziale Tasks (TestHard).'
            ms.sendMail(currentTask['name'], currentTask['email'], content)
        print 'Task %s done!' % tasks[0]['name']
    time.sleep(5)
    
