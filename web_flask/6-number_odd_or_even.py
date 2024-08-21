#!/usr/bin/python3
"""Flask Web Application - Personalized Version

The application runs on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello, HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the text.
    /python/(<text>): Displays 'Python' followed by the text.
    /number/<n>: Displays 'n is a number' if n is an integer.
    /number_template/<n>: Displays an HTML page if n is an integer.
        - Shows the value of n on the page.
    /number_odd_or_even/<n>: Displays an HTML page if n is an integer.
        - Indicates whether n is even or odd.
"""
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Define the route for the home page
@app.route("/", strict_slashes=False)
def home():
    """Returns a welcome message."""
    return "Hello, HBNB!"

# Define the route for /hbnb
@app.route("/hbnb", strict_slashes=False)
def show_hbnb():
    """Returns 'HBNB'."""
    return "HBNB"

# Define the route for /c/<text>
@app.route("/c/<text>", strict_slashes=False)
def show_c_text(text):
    """Returns 'C' followed by the text, with underscores replaced by spaces."""
    return f"C {text.replace('_', ' ')}"

# Define the routes for /python and /python/<text>
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python_text(text="is cool"):
    """Returns 'Python' followed by the text, with underscores replaced by spaces."""
    return f"Python {text.replace('_', ' ')}"

# Define the route for /number/<int:n>
@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """Returns '<n> is a number' if n is an integer."""
    return f"{n} is a number"

# Define the route for /number_template/<int:n>
@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """Renders an HTML page showing the value of n if n is an integer."""
    return render_template("5-number.html", n=n)

# Define the route for /number_odd_or_even/<int:n>
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_or_even(n):
    """Renders an HTML page indicating whether n is odd or even if n is an integer."""
    return render_template("6-number_odd_or_even.html", n=n)

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

