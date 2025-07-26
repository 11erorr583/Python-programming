# create a database using python and create users table, practice CURD ( CREATE,UPDATE, READ, DELETE)
import mysql.connector
my_database = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = ""
)
cursor = my_database.cursor()
cursor.execute(" CREATE DATABASE IF NOT EXISTS my_prac")
print(" database created ")
cursor.execute(" USE my_prac ")
print(" using database my_prac ")
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
UserId INTEGER AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(100),
email VARCHAR(1000),
password VARCHAR(100)
)


"""
 )

print(" created table users ")
query = " INSERT INTO users (Name,email,password)VALUES(%s,%s,%s)"
data = [
    ("Zubia Batool", "zubia@example.com", "securepass1"),
    ("Ayesha", "ayesha@example.com", "securepass2"),
    ("Ali", "ali@example.com", "securepass3")

]
cursor.executemany(query,data)
my_database.commit()
print(" VALUES are inserted into the table")

cursor.execute(
    """ SHOW TABLES """

)

print(" TABLES in database are: ")
for table in cursor.fetchall():
    print(table)
cursor.execute(""" SELECT * FROM users """)
print(" THE datas in table is : ")
for row in cursor.fetchall():
    print(row)


print( " UPDATE: ")
cursor.execute(""" UPDATE users SET password = 'zubia@2024' WHERE UserId = 1 """)
my_database.commit()
cursor.execute(""" SELECT * FROM users """)
print(" THE data in table is : ")
for row in cursor.fetchall():
    print(row)

    

print(" DELETE: ")
cursor.execute(""" DELETE FROM users WHERE UserId = 1""")
my_database.commit()
print(" THE data in table is : ")
cursor.execute(""" SELECT * FROM users """)
for row in cursor.fetchall():
    print(row)

cursor.execute(""" TRUNCATE users """)

cursor.close()
my_database.close()