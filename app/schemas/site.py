from typing import Optional, List
from pydantic import BaseModel


class SiteBase(BaseModel):
    name: str
    address: str
    max_electric_power: int
   

class SiteDetail(SiteBase):
    id: int
    manager_id: int
    assets: Optional[List[str]] = []

    class Config:
        orm_mode = True