#Create a database for the login of the catCafe
#This database should identify the user by their username and password
#Differentiate between the user and the admin
#The user should send to opcioCafe-Usuario-html after lign
#The admin should send to opcioCafe-Admin-html after lign

import sqlite3
import os
import hashlib
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

#Create the database
def createDB():
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin INTEGER)''')
    conn.commit()
    conn.close()

#Insert a new user
def insertUser(username, password, admin):
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users VALUES (?, ?, ?)''', (username, password, admin))
    conn.commit()
    conn.close()

#Check if the user exists
def checkUser(username, password):
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    user = c.fetchone()
    conn.close()
    return user

#Check if the user is admin
def checkAdmin(username):
    conn = sqlite3.connect('catCafe.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE username = ?''', (username,))
    user = c.fetchone()
    conn.close()
    return user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()
        admin = 0
        insertUser(username, password, admin)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()
        user = checkUser(username, password)
        if user:
            admin = checkAdmin(username)
            if admin[2] == 1:
                return redirect(url_for('opcioCafeAdmin'))
            else:
                return redirect(url_for('opcioCafeUsuario'))
    return render_template('login.html')

@app.route('/opcioCafe-Usuario')
def opcioCafeUsuario():
    return render_template('opcioCafe-Usuario.html')

@app.route('/opcioCafe-Admin')
def opcioCafeAdmin():
    return render_template('opcioCafe-Admin.html')

if __name__ == '__main__':
    createDB()
    app.run(debug=True)

#To run the program, type in the terminal: python3 BDcatcafe.py
#Open the browser and type: http://
#The program will show the login page
#If you don't have an account, click on register
#Fill the form and click on register
