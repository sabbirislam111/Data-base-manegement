import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sabbir1324",
    database = "mydatabase"
)

myCursor = my_db.cursor()


sql_command = """

                CREATE TABLE student(
                    name VARCHAR(30),
                    roll INT
                );


              """

myCursor.execute(sql_command)

