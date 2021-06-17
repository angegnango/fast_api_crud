from fastapi import APIRouter, status
from app.views import assets, home, managers

# Setup Router
router = APIRouter()

# Include Api endpoints
router.include_router(home.router,  tags=['home'])
router.include_router(assets.router, prefix='/api/v1/assets', tags=['assets'])
router.include_router(managers.router, prefix='/api/v1/managers', tags=['managers'])
