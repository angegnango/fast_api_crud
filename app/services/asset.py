from app.schemas.asset import AssetBase
from app.models.asset import Asset
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.services.site import site_crud
from fastapi import Depends, HTTPException, status

class AssetService:

    def get_asset(self, asset_id:int, db:Session=Depends(get_db)):
        return db.query(Asset).filter(Asset.id == asset_id).first()


    def get_asset_by_name(self, asset_name:str, db:Session=Depends(get_db)):
        return db.query(Asset).filter(Asset.name == asset_name).first()


    def fetch(self, db:Session=Depends(get_db), skip:int = 0, limit:int = 10):
        return db.query(Asset).offset(skip).limit(limit).all()


    def update(self, asset_id:int, asset:AssetBase, db:Session=Depends(get_db)):
        
        asset_to_update = self.get_asset(asset_id, db)
        nominal_electric_power = asset.nominal_electric_power

        # Apply site maximul power constraint
        if asset.site_id:
            site = site_crud.get_site(asset.site_id, db)
            if site_crud.power_capacity(site) > nominal_electric_power:
                asset_to_update.site_id = asset.site_id
            else:
                db.add(asset_to_update)
                db.commit()
                db.refresh(asset_to_update)
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        db.add(asset_to_update)
        db.commit()
        db.refresh(asset_to_update)
        return asset_to_update



    def delete(self, asset_id:int, db:Session=Depends(get_db)):
        asset_to_delete = self.get_asset(asset_id, db)
        db.delete(asset_to_delete)
        db.commit()
        return {}



    def store(self, asset:AssetBase, db:Session=Depends(get_db)):
        
        if self.get_asset_by_name(asset.name, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Asset name already exist')

        asset_created = Asset(
            name=asset.name,
            asset_type=asset.asset_type,
            nominal_electric_power=asset.nominal_electric_power
        )
        db.add(asset_created)
        db.commit()
        db.refresh(asset_created)
        return asset_created


asset_crud = AssetService()