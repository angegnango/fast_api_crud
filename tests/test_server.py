from tests.conftest import mock_client
from fastapi import status

def test_server_run_without_error(mock_client):
    """ server suite test case """
    response = mock_client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'welcome home'}