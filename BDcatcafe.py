# database.py
import sqlite3

# Create the database
def createDB():
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin INTEGER)''')
    conn.commit()
    conn.close()

# Insert a new user
def insertUser(username, password, admin):
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users VALUES (?, ?, ?)''', (username, password, admin))
    conn.commit()
    conn.close()

# Check if the user exists
def checkUser(username, password):
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    user = c.fetchone()
    conn.close()
    return user

# Check if the user is admin
def checkAdmin(username):
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE username = ?''', (username,))
    user = c.fetchone()
    conn.close()
    return user