from typing import Optional, List
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


class AssetDetail(AssetBase):
    id: int
    site_id: Optional[int] = None

    class Config:
        orm_mode = True
        use_enum_values = True