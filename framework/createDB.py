import sqlite3
import os
import sys

dbname = 'common/testHard.db'

if os.path.exists(dbname):
	print 'Database is already created.'
	sys.exit()

#with open('dbname', 'w'):
#	pass

conn = sqlite3.connect(dbname)
c = conn.cursor()
c.execute('''
	create table repositories (
		id INTEGER PRIMARY KEY,
		name TEXT,
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

c.execute("""
    insert into repositories 
    (name, url, comment, type, login, password)
    values (
        'abcd',
        'http://testhard.unfuddle.com/svn/testhard_project1/',
        'asfer',
        'svn',
        'krzychusan',
        '5120045',
    )
""")

conn.commit()
conn.close()

print 'Database', dbname, 'created.'
