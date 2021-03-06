# -*- coding: utf-8 -*-


"""
Flask web server responsible for serving REST (JSON) API.
"""

import flask

# -*- coding: utf-8 -*-

"""
The server (backend) code to manage (fectch, store) the broadcast schedules.

This subpackage may be later moved to standalone repository.

__Features__
- [ ] Fetch the schedule from the REST service and show the result.
- [ ] Allow to save the result to the database.
      Check wneever the schedules are already saved.
- [ ] Allow to manage stored schedules.
      Must be specified
"""

import datetime as dt
import logging

import flask
from cro.schedule import Client
from flask import Blueprint, request
from flask_wtf.csrf import CSRFProtect

__all__ = tuple(["main"])


# ########################################################################
#
# ########################################################################


class Application:
    """
    The Flask based application server.
    """

    def __init__(self, configuaration, client):
        self.configuration = configuaration
        self.client = client

    @classmethod
    def make(cls):

        from cro.schedule.__server.api import api_bp
        from cro.schedule.__server.home import home_bp

        app = flask.Flask(__name__, template_folder="./templates")

        app.register_blueprint(api_bp)
        app.register_blueprint(home_bp)

        app.config.update(
            SECRET_KEY="secret_sauce",
            SESSION_COOKIE_SECURE=True,
            SESSION_COOKIE_HTTPONLY=True,
            SESSION_COOKIE_SAMESITE="Lax",
            TEMPLATES_AUTO_RELOAD=True,
        )

        return app

    @classmethod
    def run(cls):
        logging.basicConfig(level=logging.DEBUG)
        # csrf = CSRFProtect()
        # csrf.init_app(app)
        app = cls.make_server()
        app.run(debug=True, use_debugger=False, use_reloader=False)
