__author__ = "Arjun"

from flask import Flask, render_template, request, session
from src.models.user import User

# telling python that we are creating a flask application
app = Flask(__name__)   # built in variable

# creating the API's end point
@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/login')
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)

    return render_template("profile.html", email="hello")


if __name__ == '__main__':
    app.run(port=4994)
