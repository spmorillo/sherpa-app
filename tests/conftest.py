import pytest
import flask

from sherpa_app import webapp

@pytest.fixture
def client():
    webapp.app.testing = True
    with webapp.app.test_client() as client:
        yield client