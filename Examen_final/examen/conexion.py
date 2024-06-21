import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "Login"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Login")
cursor.execute("USE Login")
db.commit()
cursor.close()
db.close()
