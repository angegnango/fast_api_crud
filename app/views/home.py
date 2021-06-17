from fastapi import APIRouter, status

# Setup Router
router = APIRouter()

# Handle home page view
@router.get('/', status_code=status.HTTP_200_OK)
async def home():
    return {'message': 'welcome home'}