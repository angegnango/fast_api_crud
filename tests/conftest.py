import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth import AuthService

@pytest.fixture(scope="module")
def mock_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def auth_handler():
    service = AuthService()
    return service