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
        test_cmds TEXT,
        test_results TEXT
	)
''')
conn.commit()
conn.close()

print 'Database', dbname, 'created.'
