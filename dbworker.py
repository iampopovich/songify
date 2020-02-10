import sqlite3
#В дбворкер можно прокинуть совершенно любой запрос . как-то надо экранировать левые запросы

def getConnection(database):
	try:
		connection = sqlite3.connect(database)
		if validateDatabase(connection): return connection
		else: 
			print("Seems like something wrong with database file...")
			sys.exit(0)
	except Exception as e:
		return e

def validateDatabase(connection):
	# cursor = connection.cursor()
	# query = "select * from "
	# tables = cursor.execute(query)
	# if ["users","songs"].sort() == tables.fetchall().sort():
	# 	return True
	return True #return True by default till i find a way to validate database file
	pass

#return bool if information exists or not 
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

