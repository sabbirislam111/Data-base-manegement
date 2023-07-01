import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sabbir1324",
    database = "mydatabase"
)

myCursor = my_db.cursor()


sql_command = """

                INSERT INTO student(name, roll)
                VALUES("sabbir", 12),("sadia", 23)


              """

myCursor.execute(sql_command)
my_db.commit()