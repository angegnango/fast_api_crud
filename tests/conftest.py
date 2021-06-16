import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def mock_client():
    with TestClient(app) as client:
        yield client