from tests.conftest import mock_client
from fastapi import status
from app.services.auth import auth

# Get access token for testing
access_token:str = auth.get_access_token('user@test.com')

def test_manager_asset_unauthenticated(mock_client):
    """ post manager suite test case for unauthenticated """

    mock_manager = {
        'last_name': 'John',
        'first_name': 'Doe'
    }

    response = mock_client.post('/api/v1/managers',
        headers={'Authorization': 'Bearer token'},
        json = mock_manager,
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED