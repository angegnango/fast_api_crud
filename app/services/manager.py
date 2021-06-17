from app.schemas.manager import ManageBase
from app.models.manager import Manager
from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

class ManagerService:

    def get_manager(self, manager_id:int, db:Session=Depends(get_db)):
        return db.query(Manager).filter(Manager.id == manager_id).first()


    def get_manager_by_first_name(self, first_name:str, db:Session=Depends(get_db)):
        return db.query(Manager).filter(Manager.first_name == first_name).first()


    def fetch(self, db:Session=Depends(get_db), skip:int = 0, limit:int = 10):
        return db.query(Manager).offset(skip).limit(limit).all()


    def update(self, manager_id:int, manager:ManageBase, db:Session=Depends(get_db)):
        manager_to_update = self.get_manager(manager_id, db)
        manager_to_update.last_name = manager.last_name
        db.add(manager_to_update)
        db.commit()
        db.refresh(manager_to_update)
        return manager_to_update



    def delete(self, manager_id:int, db:Session=Depends(get_db)):
        manager_to_delete = self.get_manager(manager_id, db)
        db.delete(manager_to_delete)
        db.commit()
        return {}



    def store(self, manager:ManageBase, db:Session=Depends(get_db)):
        
        if self.get_manager_by_first_name(manager.first_name, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Manager already exist')

        manager_created = Manager(
            first_name=manager.first_name,
            last_name=manager.last_name
        )
        db.add(manager_created)
        db.commit()
        db.refresh(manager_created)
        return manager_created


manager_crud = ManagerService()