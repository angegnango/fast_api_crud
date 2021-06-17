from tests.conftest import mock_client
from fastapi import status
from app.services.auth import auth

# Get access token for testing
access_token:str = auth.get_access_token('user@test.com')

def test_post_site_unauthenticated(mock_client):
    """ post site suite test case for unauthenticated """

    mock_site = {
        'name': 'JKS',
        'address': 'Paris',
        'max_electric_power': 1000
    }

    response = mock_client.post('/api/v1/sites',
        headers={'Authorization': 'Bearer token'},
        json = mock_site,
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_post_manager(mock_client):
    """ post manager suite test case for authenticated """

    mock_site = {
        'name': 'JKS',
        'address': 'Paris',
        'max_electric_power': 1000
    }

    response = mock_client.post(
        '/api/v1/sites',
        headers={'Authorization': f'Bearer {access_token}'},
        json = mock_site,
    )

    assert response.status_code == status.HTTP_201_CREATED


    
def test_fetch_sites(mock_client):
    """ fetch manager suite case for authenticated user """

    response = mock_client.get('/api/v1/sites', headers={'Authorization': f'Bearer {access_token}'},)
    assert response.status_code == status.HTTP_200_OK


def test_update_sites(mock_client):
    """ update site suite case for authenticated user """

    new_site = {
        'name': 'JKS',
        'address': 'Paris',
        'max_electric_power': 2000,
        'manager_id': 1
    }

    response = mock_client.put(
        '/api/v1/sites/1',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_site,
    )

    assert response.status_code == status.HTTP_201_CREATED


def test_delete_site(mock_client):
    """ delete site suite case for authenticated user """

    response = mock_client.delete(
        '/api/v1/sites/1',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_asset_to_site(mock_client):
    """ add asset to site suite case for authenticated user """

    # Create Site
    mock_site = {
        'name': 'JKS',
        'address': 'Paris',
        'max_electric_power': 1000
    }

    response = mock_client.post(
        '/api/v1/sites',
        headers={'Authorization': f'Bearer {access_token}'},
        json = mock_site,
    )

    # Create Asset
    new_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 23
    }

    response = mock_client.post(
        '/api/v1/assets',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_asset,
    )
    
    # Update Asset
    new_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 23,
        'site_id':1
    }

    response = mock_client.put(
        '/api/v1/assets/1',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_asset,
    )

    assert response.status_code == status.HTTP_201_CREATED


def test_asset_to_site_with_highest_power(mock_client):
    """ add asset to site suite case for authenticated user with highest power """

    # Create Site
    mock_site = {
        'name': 'JKS',
        'address': 'Paris',
        'max_electric_power': 1000
    }

    response = mock_client.post(
        '/api/v1/sites',
        headers={'Authorization': f'Bearer {access_token}'},
        json = mock_site,
    )

    # Create Asset
    new_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 2000
    }

    response = mock_client.post(
        '/api/v1/assets',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_asset,
    )
    
    # Update Asset
    new_asset = {
        'name': 'asset',
        'asset_type': 'compressor',
        'nominal_electric_power': 2000,
        'site_id':1
    }

    response = mock_client.put(
        '/api/v1/assets/1',
        headers={'Authorization': f'Bearer {access_token}'},
        json = new_asset,
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN