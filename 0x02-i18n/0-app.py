#!/usr/bin/env python3
"""Basic Flask app
   First you will setup a basic Flask app
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def get_index() -> str:
    """The home/index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)