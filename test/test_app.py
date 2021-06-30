import pytest
from app import app


@pytest.fixture
def client():
    """
    Test client used for simulating requests
    """

    return app.test_client()


def test_home(client):

    response = client.get('/')
    assert response.status_code == 200


def test_metrics(client):

    response = client.get('/metrics')
    assert response.status_code == 200


def test_status(client):

    response = client.get('/status')
    assert response.status_code == 200
