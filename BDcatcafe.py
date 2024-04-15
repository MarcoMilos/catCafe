import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def createDB():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password"
    )
    c = conn.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS catCafe")
    conn.commit()
    conn.close()

def insertUser(username, password, admin):
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="catCafe"
    )
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (%s, %s, %s)", (username, password, admin))
    conn.commit()
    conn.close()

def checkUser(username, password):
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="catCafe"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def checkAdmin(username):
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="catCafe"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = c.fetchone()
    conn.close()
    return user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = checkUser(username, password)
        if account:
            session['loggedin'] = True
            session['username'] = account[0]
            msg = 'Logged in successfully!'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)



#Insert for the database
#INSERT INTO users (username, password, admin) VALUES ('Alex', 'password1', 0);
#INSERT INTO users (username, password, admin) VALUES ('Franco', 'password2', 0);
#INSERT INTO users (username, password, admin) VALUES ('Marco', 'adminpassword1', 1);
#INSERT INTO users (username, password, admin) VALUES ('Pedro', 'adminpassword2', 1);