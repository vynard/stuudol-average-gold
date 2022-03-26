import sqlite3

db = sqlite3.connect('userdata.db')
c = db.cursor()

c.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    user_name TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT
    classes TEXT
) 
""")

db.commit()
db.close()