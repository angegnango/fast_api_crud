from tests.conftest import mock_client
from fastapi import status

def test_server_run_without_error(mock_client):
    """ server suite test case """
    response = mock_client.get('/api/v1/token')
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json().get('token'), str) 