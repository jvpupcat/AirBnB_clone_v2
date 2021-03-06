#!/usr/bin/python3
# script that starts a Flask web application

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
def python_defaultmsg():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def if_number(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        return render_template(
            '6-number_odd_or_even.html', number=n, statement="even")
    else:
        return render_template(
            '6-number_odd_or_even.html', number=n, statement="odd")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
