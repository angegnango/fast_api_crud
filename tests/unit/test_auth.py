from tests.conftest import auth_handler
    
def test_get_access_token(auth_handler):
    """ get access token suite case """

    email:str = 'user@test.com'
    access_token = auth_handler.get_access_token(email)
    assert isinstance(access_token.split('.'), list)


def test_hash_password(auth_handler):
    """ hash password suite case """

    password:str ='password'
    hashed_password = auth_handler.hash_password(password)
    assert hashed_password != password
    assert auth_handler.verify_password(password, hashed_password)