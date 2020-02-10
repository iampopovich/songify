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
		connection.close()
		return e

def validateDatabase(database):
	# cursor = connection.cursor()
	# query = "select * from "
	# tables = cursor.execute(query)
	# if ["users","songs"].sort() == tables.fetchall().sort():
	# 	return True
	return True #return True by default till i find a way to validate database file
	pass

#return bool if information exists or not 
def checkData(database,query):
	try:
		connection = getConnection(database)
		cursor = connection.cursor()
		cursor.execute(query)
		return len(cursor.fetchall()) != 0
	except Exception as ex:
		raise ex
	finally:
		connection.close()

#return dataset if it exists 
def getData(database, query):
	try:
		connection = getConnection(database)
		cursor = connection.cursor()
		cursor.execute(query)
		return cursor.fetchall()
	except Exception as ex:
		raise ex
	finally:
		connection.close()

def insertData(database, query):
	try:
		connection = getConnection(database)
		cursor = connection.cursor()
		cursor.execute(query)
		connection.commit()
		connection.close()
	except Exception as ex:
		raise ex
	finally:
		connection.close()

def uploadData(database):
	pass

def closeCOnnection(database):
	connection.close()
	return None

