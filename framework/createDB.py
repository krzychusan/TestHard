import sqlite3
import os
import sys

dbname = 'common/testHard.db'

if os.path.exists(dbname):
    os.remove(dbname)

conn = sqlite3.connect(dbname)
c = conn.cursor()
c.execute('''
	create table repositories (
		id INTEGER PRIMARY KEY,
		name TEXT UNIQUE,
		url TEXT,
		comment TEXT,
		type TEXT,
		login TEXT,
		password TEXT,
        build_cmd TEXT,
        find_tests_cmd TEXT,
        run_test_cmd TEXT
	)
''')

c.execute('''
    create table tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        repository TEXT,
        test_time DATETIME,
        email TEXT,
        comment TEXT
    )
''')

c.execute('''
   create table tests (
        id INTEGER PRIMARY KEY
   )
''')

c.execute("""
    insert into repositories 
    (name, url, comment, type, login, password)
    values (
        'abcd',
        'http://testhard.unfuddle.com/svn/testhard_project1/',
        'asfer',
        'svn',
        'krzychusan',
        '5120045'
    )
""")

c.execute("""
   insert into repositories
   (name, url, comment, type)
   values (
        'TestHard',
        'svn://svnhub.com/krzychusan/TestHard.svn',
        'TestHard read-only repository',
        'svn'
   )
""")

c.execute("""
   insert into tasks
   (name, test_time, email, repository)
   values (
        'SimpleCheck',
        '12-01-2011 00:45:00',
        'admin@tomaszow.com',
        'abcd'
   )
""")

conn.commit()
conn.close()

print 'Database', dbname, 'created.'
