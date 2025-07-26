# Write a script that takes input and sanitizes it before inserting into DB
import mysql.connector
import re
import datetime
from datetime import date

my_DB = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = ""
)

cursor = my_DB.cursor()
cursor.execute("""
   CREATE DATABASE IF NOT EXISTS UserInput 
""")
cursor.execute("USE UserInput")
cursor.execute("""
 CREATE TABLE IF NOT EXISTS inputs(
 id INTEGER AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(1000),
 Date_of_Birth  DATE,
 email VARCHAR(1000)
 )
""")

while True:
    print("2: Exit, 1: Continue")
    choise = input("Want to enter data : ").strip()
    
    if choise == "2":
        break
    
    elif choise == "1":
        # Sanitize name
        while True:
            Name = input("Enter your name: ").strip()
            if len(Name) > 100:
                print("The name is too long.")
            elif not re.match(r"^[A-Za-z .'-]+$", Name):
                print("Name must not contain special characters or numbers.")
            else:
                break
        print(Name)

        # Sanitize Date of Birth
        while True:
            DoB = input("Enter your date of birth (YYYY-MM-DD): ").strip()
            try:
                dob = datetime.datetime.strptime(DoB, "%Y-%m-%d").date()
                today = datetime.date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 10:
                    print("Error ⚔️  Age must be greater than 10.") 
                else:
                    break       
            except ValueError:
                print("Enter correct format as YYYY-MM-DD.")
        print(DoB)

        # Sanitize email
        while True:
            mail = input("Enter your email: ").strip()
            if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', mail):
                domain = mail.split('@')[1]
                if domain.lower() != 'gmail.com':
                    print("Only Gmail account is valid.")
                else:
                    break
            else:
                print("Invalid email address.")
        print(mail)

        # Insert into database
        query = f"INSERT INTO inputs(name, Date_of_Birth, email) VALUES ('{Name}', '{DoB}', '{mail}')"
        cursor.execute(query)
        my_DB.commit()
# stimulating sql injection attack
good = input("Enter your name ")
query="SELECT * FROM inputs WHERE name = %s"
cursor.execute(query,(good,))
for row in cursor.fetchall():
    print(row)
cursor.execute(" TRUNCATE inputs")
cursor.close()
my_DB.close()