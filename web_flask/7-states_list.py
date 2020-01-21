#!/usr/bin/python3
"""
Hello flask module
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    List states in a jinja template
    """
    result = storage.all("State")
    return render_template('7-states_list.html', states=result)


@app.teardown_appcontext
def tear_down(self):
    """
    Closes the storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
