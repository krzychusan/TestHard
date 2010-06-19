import sqlite3
import os
from serwer.IRepository import IRepository

path = '/'+'/'.join(os.path.abspath(__file__).split('/')[1:-1])
dbname = path + '/testHard.db'

def connect():
	return sqlite3.connect(dbname)

def taskId(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        select id from tasks
        where name = ?
    """,(name,))
    for row in cur:
        conn.close()
        return row[0]
    conn.close()
    return None


def getCount(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select count(*) from
    ''' + name)
    for row in cur:
        conn.close()
        return row[0]
    conn.close()

def getUnfinishedTasks():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            test_time,
            comment,
            email,
            repository,
            failures_count,
            errors_count,
            tests_count,
            log,
            time_elapsed,
            timestamp
        from tasks as ts 
        left outer join results 
        on ts.id = task
        where timestamp = NULL
        order by test_time 
        limit 1
    ''')
    tasksDict = []
    for row in cur:
        tasksDict.append( 
           setUpTask(row)
        )
    conn.close()
    return tasksDict


def updateRepository(oldName, values):
    conn = connect()
    cur = conn.cursor()
    if oldName != values[0] and len(getRepositoryByName(values[0])) != 0:
        return False

    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        update repositories
        set
            name = ?,
            url = ?,
            comment = ?,
            type = ?,
            login = ?,
            password = ?,
            build_cmd = ?,
            find_tests_cmd = ?,
            run_test_cmd = ?
        where name = ?
    """, values + (oldName,))
    conn.commit()
    conn.close()
    updateTasks(oldName, values[0])
    return True

def updateTasks(oldName, newName):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
        update tasks
        set 
            repository = ?
        where repository = ?
    """, (newName, oldName))
    
    conn.commit()
    conn.close()

def addRepository(values):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        insert into repositories
        (name, url, comment, type, login, password, build_cmd, find_tests_cmd, run_test_cmd)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', values)
    conn.commit()
    conn.close()

def setUpRepositoryObject(row):
    repo = IRepository()
    repo.assign(row[0], row[1], row[2], row[3])
    if row[4] and len(row[4]) > 0:
        repo.setAuth(row[4], row[5])
    repo.setTestAttributes(row[6], row[7], row[8])
    return repo

def removeTask(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        delete from tasks
        where name = ?
    ''',(name,))
    conn.commit()
    conn.close()

def addTask(values):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        insert into tasks 
        (name, test_time, comment, email, repository) 
        values (?, ?, ?, ?, ?)
    ''', values)
    conn.commit()
    conn.close()

def addResult(values):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        insert into results
        (timestamp, task, failures_count, errors_count, tests_count, log, time_elapsed)
        values (datetime('now','localtime'), ?, ?, ?, ?, ?, ?)
    ''', values)
    conn.commit()
    conn.close()

def setUpTask(row):
    return  {
        'name' : row[0],
        'test_time' : row[1],
        'comment' : row[2],
        'email' : row[3],
        'repository' : row[4],
        'failures_count' : row[5],
        'errors_count' : row[6],
        'tests_count' : row[7],
        'log' : row[8],
        'time_elapsed' : row[9],
        'timestamp' : row[10]
     }

def getTasks():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            test_time,
            comment,
            email,
            repository,
            failures_count,
            errors_count,
            tests_count,
            log,
            time_elapsed,
            timestamp
        from tasks as ts 
        left outer join results 
        on ts.id = task
    ''')
    tasksDict = []
    for row in cur:
        tasksDict.append( 
           setUpTask(row)
        )
    conn.close()
    return tasksDict

def getTaskByName(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            test_time,
            comment,
            email,
            repository,
            failures_count,
            errors_count,
            tests_count,
            log,
            time_elapsed,
            timestamp
        from tasks as ts
        left outer join results 
        on ts.id = task
        where name = ?
    ''', (name,))
    for row in cur:
        conn.close()
        return setUpTask(row)
    conn.close()
    return None

def getRepositoryByName(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            url,
            comment,
            type,
            login,
            password,
            build_cmd,
            find_tests_cmd,
            run_test_cmd
        from repositories
        where name=?
    ''', (name,))
    repoList = []
    for row in cur:
        repoList.append(setUpRepositoryObject(row))
    conn.close()
    return repoList
 
def removeRepository(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        delete from repositories 
        where name=?
        ''', (name,))
    conn.commit()
    conn.close()

def getRepositories():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            url,
            comment,
            type,
            login,
            password,
            build_cmd,
            find_tests_cmd,
            run_test_cmd
        from repositories 
    ''')
    repoList = []
    for row in cur:
        repoList.append(setUpRepositoryObject(row))
    conn.close()
    return repoList
