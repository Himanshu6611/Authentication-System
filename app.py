from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"  # Needed for session

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Himanshu@2006#",
    database="userlogin"
)
cursor = db.cursor(dictionary=True)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                font-family: Arial;
                background: #eef2f3;
                text-align: center;
                padding-top: 100px;
            }
            a {
                background: #3498db;
                padding: 10px 18px;
                color: white;
                border-radius: 6px;
                text-decoration: none;
                margin: 0 10px;
            }
            a:hover {
                background: #217dbb;
            }
        </style>
    </head>
    <body>
        <h2>Welcome to Biometric Traits Lab!</h2>
        <a href='/signup'>Register</a>
        <a href='/login'>Login</a>
    </body>
    </html>
    """

# ---------------- SIGNUP ----------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return "❌ Username already exists, choose another."

        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            return "❌ Email already registered, use another."

        # Insert new user
        cursor.execute(
            "INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)",
            (name, username, email, password)
        )
        db.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            # Save found user temporarily (without login yet)
            session['temp_user'] = user
            return redirect(url_for('enter_password'))
        else:
            return "❌ Username not found!"
    return render_template('login.html')

# ---------------- ENTER PASSWORD ----------------
@app.route('/enter-password', methods=['GET', 'POST'])
def enter_password():
    if 'temp_user' not in session:
        return redirect(url_for('login'))

    user = session['temp_user']

    if request.method == 'POST':
        password = request.form['password']

        if user['password'] == password:
            # Success: move to logged-in session
            session['user'] = user
            session.pop('temp_user', None)
            return redirect(url_for('dashboard'))
        else:
            return "❌ Wrong password!"

    return render_template('enter_password.html')

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"✅ Welcome {session['user']['name']}!"
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
