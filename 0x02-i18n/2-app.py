#!/usr/bin/env python3

"""
Gets locale from a request
"""

from flask import Flask, render_template, request
from flask_babel import Babel

from config import Config

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Gets locale from a request
    """

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    The index page route, renders the '2-index.html' template
    """

    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
