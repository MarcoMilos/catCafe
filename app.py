from flask import Flask, render_template, request, redirect, url_for, session
from database import createDB, insertUser, checkUser, checkAdmin

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace with your secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = request.form.get('admin', 0)  # 0 if admin checkbox is not checked, 1 otherwise
        insertUser(username, password, admin)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = checkUser(username, password)
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if 'username' in session and checkAdmin(session['username']):
        return 'Welcome, admin!'
    else:
        return 'You are not an admin.'

if __name__ == '__main__':
    createDB()
    app.run(debug=True)