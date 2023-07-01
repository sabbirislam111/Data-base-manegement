import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sabbir1324",
    database = "mydatabase"
)

myCursor = my_db.cursor()


sql_command = """

                UPDATE student
                SET name = "nirob"
                WHERE roll = 12


              """

myCursor.execute(sql_command)
my_db.commit()

