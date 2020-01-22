#!/usr/bin/python3
"""
Hello flask module
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def all_states():
    """
    List all states
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    context = {'states': states, 'amenities': amenities}
    return render_template('10-hbnb_filters.html', **context)


@app.teardown_appcontext
def tear_down(self):
    """
    Closes the storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
