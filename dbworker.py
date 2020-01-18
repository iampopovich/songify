import sqlite3

def getConnection(database):
	try:
		return sqlite3.connect(database)
	except Exception as e:
		return e

def insertData(connection):
	pass

def uploadData(connection):
	pass

def closeCOnnection(connection):
	connection.close()
	return None

