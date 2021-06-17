from jose import jwt
from app.config.utils import settings
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthService:

    security = HTTPBearer()
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self,
        secret:str=settings.get('JWT_SECRET', 'secret'),
        algorithm:str=settings.get('JWT_ALGORITHM', 'HS256')):
        self.JWT_SECRET = secret
        self.JWT_ALGORITHM = algorithm


    def hash_password(self, plain_password:str):
        """ hash password handler
        param (str) : plain password
        return (str) : hashed password
        """
        return self.password_context.hash(plain_password)

    
    def verify_password(self, plain_password:str, hashed_password:str):
        """ password verification handler 
        param1 (str) : plain password
        param2 (str) : hashed password
        return (bool) : verification result
        """
        return self.password_context.verify(plain_password, hashed_password)


    def get_access_token(self, user_email:str):
        """ access token handler 
        param (str) : user email 
        return (str) : access token 
        """
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=3),
            'iat': datetime.utcnow(),
            'sub': user_email
        }

        access_token = jwt.encode(payload, self.JWT_SECRET, algorithm=self.JWT_ALGORITHM)
        return access_token

    
    def verify_token(self, token:str):
        """ verify token handler 
        param (str) : access token generate 
        return (dict) : verification result can be payload or error object
        """
        try:
            payload = jwt.decode(token, self.JWT_SECRET, algorithms=[self.JWT_ALGORITHM])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail='Invalid Token')

    
    def middleware(self, auth: HTTPAuthorizationCredentials=Security(security)):
        """ authentication middleware """
        return self.verify_token(auth.credentials)
        
auth = AuthService()
    