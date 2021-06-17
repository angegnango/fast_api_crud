from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from app.schemas.manager import ManageBase, ManageDetail
from app.models.manager import Manager
from app.services.manager import manager_crud
from app.services.auth import auth
from typing import List

# Setup Router
router = APIRouter()

# Handle Crud

@router.get('', status_code= status.HTTP_200_OK, response_model=List[ManageDetail])
async def fetch(db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return manager_crud.fetch(db)


@router.post('', status_code= status.HTTP_201_CREATED, response_model=ManageDetail)
async def post(manager:ManageBase, db:Session=Depends(get_db), user:str=Depends(auth.middleware) ):
    return manager_crud.store(manager, db)


@router.put('/{manager_id}', status_code= status.HTTP_201_CREATED, response_model=ManageDetail)
async def update(manager_id:int, manager:ManageBase, db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return manager_crud.update(manager_id, manager, db)


@router.delete('/{manager_id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete(manager_id:int, db:Session=Depends(get_db), user:str=Depends(auth.middleware)):
    return manager_crud.delete(manager_id, db)