from gevent import monkey

monkey.patch_all(thread=False)

import pytest
from flask.testing import FlaskClient

from app import create_app
from .utils import JSONResponse


@pytest.fixture(scope='module')
def flask_app():
    app = create_app(environment='testing')
    yield app


@pytest.fixture(scope='module')
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    app.response_class = JSONResponse
    return app.test_client()
