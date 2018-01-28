from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
	try:
		conn = MySQLdb.connect(user="root",passwd="*******",host="localhost",db="mydb") 
		cur = conn.cursor()
		cur.execute("show tables")
		return "Database: world:: " + str(cur.fetchall())
	except Exception as e:
		return (str(e))
	finally:
		cur.close()
		conn.close()

if __name__ == "__main__":
	app.run(debug=True)
