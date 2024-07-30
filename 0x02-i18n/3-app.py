#!/usr/bin/env python3

"""
Parametrized templatess
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

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    The index page route, renders the '3-index.html' template
    """

    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
