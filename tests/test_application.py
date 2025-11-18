import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from application import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World from Flask and Elasticbeanstalk!" in response.data