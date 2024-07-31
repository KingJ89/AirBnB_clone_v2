#!/usr/bin/python3
"""Starts a Flask web application with various routes."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Display 'HBNB'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Display 'C' followed by <text> with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """Display 'Python' followed by <text> with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Display '<n> is a number' if <n> is an integer."""
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """Render an HTML page with <n> if <n> is an integer."""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
