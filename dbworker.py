import sqlite3
#В дбворкер можно прокинуть совершенно любой запрос . как-то надо экранировать левые запросы

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
def checkData(connection,query):
	cursor = connection.cursor()
	cursor.execute(query)
	return len(cursor.fetchall()) != 0

#return dataset if it exists 
def getData(connection, query):
	cursor = connection.cursor()
	cursor.execute(query)
	return cursor.fetchall()

def insertData(connection, query):
	try:
		cursor = connection.cursor()
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

