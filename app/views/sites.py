from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from app.schemas.site import SiteBase, SiteDetail
from app.models.site import Site
from app.services.site import site_crud
from app.services.auth import auth
from typing import List

# Setup Router
router = APIRouter()

# Handle Crud

@router.get('', status_code= status.HTTP_200_OK, response_model=List[SiteDetail])
async def fetch(db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return site_crud.fetch(db)


@router.post('', status_code= status.HTTP_201_CREATED, response_model=SiteDetail)
async def post(site:SiteBase, db:Session=Depends(get_db), user:str=Depends(auth.middleware) ):
    return site_crud.store(site, db)


@router.put('/{site_id}', status_code= status.HTTP_201_CREATED, response_model=SiteDetail)
async def update(site_id:int, site:SiteBase, db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return site_crud.update(site_id, site, db)


@router.delete('/{site_id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete(site_id:int, db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return site_crud.delete(site_id, db)