from fastapi import APIRouter, status
from app.services.auth import auth

# Setup Router
router = APIRouter()

# Handle home page view
@router.get('/', status_code=status.HTTP_200_OK)
async def get_token():
    email:str ='user@test.com'
    access_token = auth.get_access_token(email)
    return {'token': access_token}