from typing import Optional, List
from pydantic import BaseModel


class ManageBase(BaseModel):
    fist_name: str
    last_name: str
   

class ManageDetail(ManageBase):
    id: int

    class Config:
        orm_mode = True
    