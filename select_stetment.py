import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sabbir1324",
    database = "hr"
)

myCursor = my_db.cursor()


sql_command = """

                SELECT *
                FROM employees


              """

myCursor.execute(sql_command)

data = myCursor.fetchall()

for i in data:
    print(i)