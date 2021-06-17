from tests.conftest import mock_client
from fastapi import status
from app.services.auth import auth

# Get access token for testing
access_token:str = auth.get_access_token('user@test.com')

def test_post_manager_unauthenticated(mock_client):
    """ post manager suite test case for unauthenticated """

    mock_manager = {
        'first_name': 'Doe',
        'last_name': 'John'
    }

    response = mock_client.post('/api/v1/managers',
        headers={'Authorization': 'Bearer token'},
        json = mock_manager,
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_post_manager(mock_client):
    """ post manager suite test case for authenticated """

    mock_manager = {
        'last_name': 'John',
        'first_name': 'Doe'
    }

    response = mock_client.post(
        '/api/v1/managers',
        headers={'Authorization': f'Bearer {access_token}'},
        json = mock_manager,
    )

    assert response.status_code == status.HTTP_201_CREATED


    
def test_fetch_managers(mock_client):
    """ fetch manager suite case for authenticated user """

    response = mock_client.get('/api/v1/managers', headers={'Authorization': f'Bearer {access_token}'},)
    assert response.status_code == status.HTTP_200_OK


def test_update_manager(mock_client):
    """ update asset suite case for authenticated user """

    new_manager = {
        'last_name': 'John',
        'first_name': 'Elvis'
    }

    response = mock_client.put(
        '/api/v1/managers/1',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_manager,
    )

    assert response.status_code == status.HTTP_201_CREATED


def test_delete_manager(mock_client):
    """ delete manager suite case for authenticated user """

    response = mock_client.delete(
        '/api/v1/managers/1',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT