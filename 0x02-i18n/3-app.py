#!/usr/bin/env python3
"""
Define a Flask app that implements Babel
for i18n.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuration for Babel. """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route(
        "/",
        strict_slashes=False
        )
def index():
    """
    Handle requests to the root directory.
    """
    return (render_template("3-index.html"))


@babel.localeselector
def get_locale():
    """
    Find the best language match based
    on the user's locale.
    """
    return (request.accept_languages.best_match(app.config["LANGUAGES"]))