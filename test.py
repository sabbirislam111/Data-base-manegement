import mysql.connector

mybd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sabbir1324"
)

myCursor = mybd.cursor()

dbname = "mydatabase"
sqlcomand = "CREATE DATABASE " + dbname

myCursor.execute(sqlcomand)
