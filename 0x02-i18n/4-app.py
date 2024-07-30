#!/usr/bin/env python3

"""
Implementing a way to force a particular locale by passing the 'locale=fr'
parameter to my app's URLs
"""

from typing import Union

from flask import Flask, render_template, request
from flask_babel import Babel

from config import Config

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Gets locale from a request
    """

    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    The index page route, renders the '4-index.html' template
    """

    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
