#!/usr/bin/env python3

#this project task we install flask and we create the first hello world file in flask.

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
