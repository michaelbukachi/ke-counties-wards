import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from flask import Flask

from .config import config


class Factory:

    def __init__(self, environment='development'):
        self._environment = os.environ.get('APP_ENVIRONMENT', environment)
        self.flask: Flask = None

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, env):
        self._environment = env

    def set_flask(self, **kwargs):
        self.flask = Flask(__name__, **kwargs)
        self.flask.config.from_object(config[self._environment])
        # setup logging
        stdout = logging.StreamHandler(sys.stdout)
        stdout.setLevel(logging.DEBUG)
        self.flask.logger.addHandler(stdout)

        return self.flask

    def set_api(self):
        from .resources import api
        api.init_app(self.flask, version='1.0.0', title='County - Wards API')


