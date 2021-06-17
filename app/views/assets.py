from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from app.schemas.asset import AssetBase, AssetDetail
from app.models.asset import Asset
from app.services.asset import asset_crud
from app.services.auth import auth
from typing import List

# Setup Router
router = APIRouter()

# Handle Crud

@router.get('', status_code= status.HTTP_200_OK, response_model=List[AssetDetail])
async def fetch(db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return asset_crud.fetch(db)


@router.post('', status_code= status.HTTP_201_CREATED, response_model=AssetDetail)
async def post(asset:AssetBase, db:Session=Depends(get_db), user:str=Depends(auth.middleware) ):
    return asset_crud.store(asset, db)


@router.put('/{asset_id}', status_code= status.HTTP_201_CREATED, response_model=AssetDetail)
async def update(asset_id:int, asset:AssetBase, db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return asset_crud.update(asset_id, asset, db)


@router.delete('/{asset_id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete(asset_id:int, db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return asset_crud.delete(asset_id, db)