#!/usr/bin/python3
"""
Hello flask module
"""
from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Print a number template
    """
    if type(n) is int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_ever(n):
    """
    Tells if is odd and even
    """
    if type(n) is int:
        if n % 2 == 0:
            ctx = {'number': n, 'text': 'even'}
            return render_template('6-number_odd_or_even.html', **ctx)
        else:
            ctx = {'number': n, 'text': 'odd'}
            return render_template('6-number_odd_or_even.html', **ctx)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
