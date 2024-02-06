#!/usr/bin/env python3
"""task 2"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """render index.html"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return (request.accept_languages.best_match(app.config['LANGUAGES']))