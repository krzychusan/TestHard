import sqlite3
import os
from serwer.IRepository import IRepository

path = '/'+'/'.join(os.path.abspath(__file__).split('/')[1:-1])
dbname = path + '/testHard.db'

def connect():
	return sqlite3.connect(dbname)

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
    if len(row[4]) > 0:
        repo.setAuth(row[4], row[5])
    repo.setTestAttributes(row[6], row[7], row[8])
    return repo

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

def getTasks():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        select
            name,
            time(test_time),
            comment,
            email,
            repository
        from tasks
    ''')
    tasksList = []
    for row in cur:
        tasksList.append( {
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
