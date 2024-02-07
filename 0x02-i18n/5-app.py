#!/usr/bin/env python3
"""
Define a Flask app that implements Babel
for i18n.
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return (render_template("5-index.html"))


# @babel.localeselector
def get_locale():
    """
    Find the best language match based
    on the user's locale.
    """
    query_string = request.query_string.decode("utf-8")
    language = query_string[(query_string.find("=") + 1):]
    if (language in app.config["LANGUAGES"]):
        return (query_string[(query_string.find("=") + 1):])
    return (request.accept_languages.best_match(app.config["LANGUAGES"]))


def get_user(user_id):
    """
    returns a user dictor None if the ID cannot
    be found or if login_as was not passed.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    before_request should use get_user to find a user
    if any, and set it as a global on flask.g.user
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None
