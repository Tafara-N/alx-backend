#!/usr/bin/env python3

"""
App module
"""

from typing import Union

import pytz.exceptions
from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class for Babel
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    """
    Return
        user's dict if ID can be found
    """

    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Gets locale
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    Gets the timezone
    """

    user = get_user()
    if user:
        locale = user["timezone"]
    if request.args.get("timezone"):
        locale = request.args.get("timezone")

    try:
        return timezone(locale).zone
    except Exception:
        return None


@app.before_request
def before_request():
    """
    Before a request
    """

    g.user = get_user()


@app.route("/")
def index() -> str:
    """
    The index page route, renders the '7-index.html' template
    """

    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
