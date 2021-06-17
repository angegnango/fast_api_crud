from fastapi import APIRouter, status
from app.views import assets, auth, managers, sites

# Setup Router
router = APIRouter()

# Include Api endpoints
router.include_router(auth.router,  prefix='/api/v1/token', tags=['auth'])
router.include_router(assets.router, prefix='/api/v1/assets', tags=['assets'])
router.include_router(managers.router, prefix='/api/v1/managers', tags=['managers'])
router.include_router(sites.router, prefix='/api/v1/sites', tags=['sites'])
