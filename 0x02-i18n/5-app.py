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


@babel.localeselector
def get_locale():
    """
    Find the best language match based
    on the user's locale.
    """
    app.logger.info("emma")
    locale = request.args.get('locale', None)
    app.logger.info(locale)
    if locale in app.config["LANGUAGES"]:
        return locale
    return (request.accept_languages.best_match(app.config["LANGUAGES"]))


def get_user():
    """
    returns a user dictor None if the ID cannot
    be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    before_request should use get_user to find a user
    if any, and set it as a global on flask.g.user
    """    
    g.user = get_user()