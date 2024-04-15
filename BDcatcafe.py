import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def checkUser(username, password):
    try:
        conn = mysql.connector.connect(
            host="plpcollado.mysql.pythonanywhere-services.com",
            user="plpcollado",
            password="QD7hgXVvYNJ.Aw",
            database="plpcollado$catCafe"
        )
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = c.fetchone()
        if user:
            return {'admin': user[2]}
    except Exception as e:
        print("Failed to check user:", e)
    finally:
        conn.close()
    return None

def checkAdmin(username):
    try:
        conn = mysql.connector.connect(
            host="plpcollado.mysql.pythonanywhere-services.com",
            user="plpcollado",
            password="QD7hgXVvYNJ.Aw",
            database="plpcollado$catCafe"
        )
        c = conn.cursor()
        c.execute("SELECT admin FROM users WHERE username = %s", (username,))
        admin_status = c.fetchone()
        return admin_status[0] if admin_status else None
    except Exception as e:
        print("Failed to check admin status:", e)
    finally:
        conn.close()

def insertUser(username, password):
    try:
        conn = mysql.connector.connect(
            host="plpcollado.mysql.pythonanywhere-services.com",
            user="plpcollado",
            password="QD7hgXVvYNJ.Aw",
            database="plpcollado$catCafe"
        )
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, admin) VALUES (%s, %s, %s)", (username, password, False))
        conn.commit()
        return True
    except Exception as e:
        print("Failed to insert user:", e)
        return False
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user_info = checkUser(username, password)
        if user_info:
            return jsonify(user_info)
    return jsonify({'error': 'Incorrect username/password'})

@app.route('/register', methods=['POST'])
def register():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if insertUser(username, password):
            return jsonify({'success': True})
    return jsonify({'error': 'Failed to register user'})


if __name__ == '__main__':
    app.run(debug=True)



#Insert for the database
#INSERT INTO users (username, password, admin) VALUES ('Alex', 'password1', 0);
#INSERT INTO users (username, password, admin) VALUES ('Franco', 'password2', 0);
#INSERT INTO users (username, password, admin) VALUES ('Marco', 'adminpassword1', 1);
#INSERT INTO users (username, password, admin) VALUES ('Pedro', 'adminpassword2', 1);