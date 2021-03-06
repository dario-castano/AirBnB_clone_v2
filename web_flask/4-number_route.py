#!/usr/bin/python3
"""
Hello flask module
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Displays Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """
    Displays HBNB on route
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Prints C + <text>
    """
    return 'C ' + ' '.join(text.split('_'))


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python_is_fun(text='is cool'):
    """
    Prints Python + <text>
    """
    return 'Python ' + ' '.join(text.split('_'))


@app.route('/number/<int:n>')
def isa_number(n):
    """
    Print is a number
    """
    if type(n) is int:
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
