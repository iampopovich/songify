import sqlite3

def getConnection(database):
	try:
		return sqlite3.connect(database)
	except Exception as e:
		return e

def checkSchema(connection):
	#if schema is valid return true
	#else return false and abort connection
	pass


def insertData(connection, data):
	try:
		cursor = connection.cursor()
		query = "insert into userSongs (chatID, songName, deadlineBefore) values (%s)" %data
		cursor.execute(query)
		connection.commit()
	except Exception as e:
		print(e)
		connection.destroy()
	pass

def uploadData(connection):
	pass

def closeCOnnection(connection):
	connection.close()
	return None

