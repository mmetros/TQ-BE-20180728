import sqlite3

# Make a connection to the database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Turn on Foreign Key Support
cursor.execute("PRAGMA foreign_keys = ON")

# The Users table is the parent
# the users_data table is the child


# Create Users Table
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name text,
                email text,
                password text )
                """)


# Create Users_Data Table
cursor.execute("""CREATE TABLE IF NOT EXISTS users_data(
                id INTEGER PRIMARY KEY,
                user_id int,
                latitude float,
                longitude float,
                FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
                )""")

# Create Venues Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS venues(
                id INTEGER PRIMARY KEY,
                name text,
                latitude float,
                longitude float
                )""")

# Insert Values into users table
users = [
("Matthew", "mmetros@wesleyan.edu", "abcd"),
("Andrew", "ametros@gmail.com", "abcde"),
("Matthew", "matthew.metros@gmail.com", "abcdef")
]
cursor.executemany("INSERT INTO users VALUES (NULL,?,?,?)", users)

# Insert Values into users_data table
users_data = [
    (1, 40.749394, -73.991869),
    (2, 40.748824, -73.992320),
    (3, 40.751444, -73.990431)
]
cursor.executemany("INSERT INTO users_data VALUES (NULL,?,?,?)", users_data)

# Inser Values into venues table
venues = [
    ("starbucks", 40.748824, -73.991869)
]

cursor.executemany("INSERT INTO venues VALUES (NULL,?,?,?)",venues)



connection.commit()
connection.close()
