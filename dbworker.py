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

#return bool value if information exists or not 
def checkData(connection,table,column,data):
	cursor = connection.cursor()
	query = "select * from {0} where {1} = {2}".format(table,column,data)
	cursor.execute(query)
	return len(cursor.fetchall()) != 0

#return dataset if it exists 
def getData(connection, table, column, data):
	cursor = connection.cursor()
	query = "select * from {0} where {1} = {2}".format(table, column , data)
	cursor.execute()
	return cursor.fetchall()

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

