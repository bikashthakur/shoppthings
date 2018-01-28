import MySQLdb

def connection():
	conn = MySQLdb.connect(user="root",passwd="Thakur183*",host="localhost",db="flaskapps") 
	cur = conn.cursor()
	return cur, conn