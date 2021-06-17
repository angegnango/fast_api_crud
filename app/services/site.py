from app.schemas.site import SiteBase
from app.models.site import Site
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class SiteService:

    def get_site(self, site_id:int, db:Session):
        return db.query(Site).filter(Site.id == site_id).first()


    def get_site_by_name(self, site_name:str, db:Session):
        return db.query(Site).filter(Site.name == site_name).first()


    def fetch(self, db:Session, skip:int = 0, limit:int = 10):
        return db.query(Site).offset(skip).limit(limit).all()


    def power_capacity(self, site:Site):
        power_usage = sum([asset.nominal_electric_power for asset in site.assets])
        return site.max_electric_power - power_usage


    def update(self, site_id:int, site:SiteBase, db:Session):

        site_to_update = self.get_site(site_id, db)
        site_to_update.manager_id = site.manager_id
        site_to_update.max_electric_power = site.max_electric_power
        db.add(site_to_update)
        db.commit()
        db.refresh(site_to_update)
        return site_to_update


    def delete(self, site_id:int, db:Session):
        site_to_delete = self.get_site(site_id, db)
        db.delete(site_to_delete)
        db.commit()
        return {}


    def store(self, site:SiteBase, db:Session):
        
        if self.get_site_by_name(site.name, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Site already exist')

        site_created = Site(
            name=site.name,
            address=site.address,
            max_electric_power=site.max_electric_power
        )
        db.add(site_created)
        db.commit()
        db.refresh(site_created)
        return site_created

    


site_crud = SiteService()