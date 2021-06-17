from typing import Optional
from enum import Enum
from pydantic import BaseModel


class AssetType(str, Enum):
    compressor = 'compressor'
    chiller = 'chiller'
    rolling_chill = 'rolling_chill'


class AssetBase(BaseModel):
    name: str
    asset_type: AssetType
    nominal_electric_power: int
    site_id: Optional[int] = None


class AssetDetail(AssetBase):
    id: int
    

    class Config:
        orm_mode = True
        use_enum_values = True