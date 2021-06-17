from typing import Optional, List
from pydantic import BaseModel


class SiteBase(BaseModel):
    name: str
    address: str
    max_electric_power: int
    manager_id: Optional[int] = None
    assets: Optional[List[str]] = []
    
   
class SiteDetail(SiteBase):
    id: int
    
    class Config:
        orm_mode = True