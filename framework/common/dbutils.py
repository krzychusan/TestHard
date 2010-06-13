import sqlite3

dbname = 'testHard.db'

def connect():
	return sqlite.connect(dbname)

