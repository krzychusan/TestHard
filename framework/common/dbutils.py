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
    return True

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
        (task, failures_count, errors_count, tests_count, log)
        values (?, ?, ?, ?, ?)
    ''', values)
    conn.commit()
    conn.close()

def getTasks():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            test_time,
            comment,
            email,
            repository
        from tasks
    ''')
    tasksDict = []
    for row in cur:
        tasksDict.append( {
            'name' : row[0],
            'test_time' : row[1],
            'comment' : row[2],
            'email' : row[3],
            'repository' : row[4]
        } )
    conn.close()
    return tasksDict

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
