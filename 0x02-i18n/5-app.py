#!/usr/bin/env python3

"""
A mock user login system
"""

from os import getenv
from typing import Union

from flask import Flask, g, render_template, request
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class for Babel
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Setting the above class object as the configuration for the app
app.config.from_object("5-app.Config")


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    GET /

    Return
        The index page route, renders the '5-index.html' template
    """

    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages
    """

    # Checks if there is a locale parameter/query string
    if request.args.get("locale"):
        locale = request.args.get("locale")
        if locale in app.config["LANGUAGES"]:
            return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[dict, None]:
    """
    Returns user's dictionary if ID is not found
    """

    if request.args.get("login_as"):
        # Type casting to be able to search the user's dictionary
        user = int(request.args.get("login_as"))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """
    Finds user and sets as global on flask.g.user
    """

    g.user = get_user()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", 5000)
    app.run(host=host, port=int(port))
