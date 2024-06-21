from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Login"
)

USER_DATA = {
    "holbieC22@holbertonstudents.com": "C22daBest",
    "staff@holbertonschool.com": "holbertonFTW"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Verifico las credenciales
    if email in USER_DATA and USER_DATA[email] == password:
        return redirect(url_for('welcome', email=email))
    else:
        return "Datos incorrectos, intentar nuevamente."

@app.route('/welcome')
def welcome():
    email = request.args.get('email')
    return render_template('welcome.html', email=email)

if __name__ == '__main__':
    app.run()
    