import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_user_table =  "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,email text, password text )"

cursor.execute(create_user_table)

# add users to the table
users = [
(None, "mmetros@wesleyan.edu", "abcd"),
(None, "ametros@gmail.com", "abcde"),
(None, "matthew.metros@gmail.com", "abcdef")
]

cursor.executemany("INSERT INTO users VALUES (?,?,?)", users)

# Testing
for row in cursor.execute("SELECT * FROM users"):
    print(row)

connection.commit()
connection.close()
