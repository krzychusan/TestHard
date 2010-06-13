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
        (name, url, comment, type, login, password, test_cmds, test_results)
        values (?, ?, ?, ?, ?, ?, ?, ?)
    ''', values)
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
            test_cmds,
            test_results
        from repositories 
    ''')
    repoList = []
    for row in cur:
        repo = IRepository()
        repo.assign(row[0], row[1], row[2], row[3])
        if len(row[4]) > 0:
            repo.setAuth(row[4], row[5])
        repo.setTestAttributes(row[6], row[7])
        repoList.append(repo)
    conn.close()
    return repoList
