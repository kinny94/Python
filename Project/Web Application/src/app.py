__author__ = "Arjun"

from flask import Flask

# telling python that we are creating a flask application
app = Flask(__name__)   # built in variable

# creating the API's end point
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
