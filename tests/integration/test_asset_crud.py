from tests.conftest import mock_client
from fastapi import status
from app.services.auth import auth

# Get access token for testing
access_token:str = auth.get_access_token('user@test.com')

def test_post_asset_unauthenticated(mock_client):
    """ post asset suite test case for unauthenticated """

    mock_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 10
    }

    response = mock_client.post('/api/v1/assets',
        headers={'Authorization': 'Bearer token'},
        json = mock_asset,
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_post_asset(mock_client):
    """ post asset suite test case for authenticated """

    mock_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 10
    }

    response = mock_client.post(
        '/api/v1/assets',
        headers={'Authorization': f'Bearer {access_token}'},
        json = mock_asset,
    )

    assert response.status_code == status.HTTP_201_CREATED

    
def test_fetch_asset(mock_client):
    """ fetch asset suite case for authenticated user """

    response = mock_client.get('/api/v1/assets', headers={'Authorization': f'Bearer {access_token}'},)
    assert response.status_code == status.HTTP_200_OK


def test_update_asset(mock_client):
    """ update asset suite case for authenticated user """

    new_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 23
    }

    response = mock_client.put(
        '/api/v1/assets/1',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_asset,
    )

    assert response.status_code == status.HTTP_201_CREATED


def test_delete_asset(mock_client):
    """ delete asset suite case for authenticated user """

    response = mock_client.delete(
        '/api/v1/assets/1',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT

    