#!/usr/bin/env python3
"""
app with single route
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    """
    render index.html
    """
    return render_template('0-index.html')
