from pydantic import BaseModel


class ManageBase(BaseModel):
    first_name: str
    last_name: str
   

class ManageDetail(ManageBase):
    id: int

    class Config:
        orm_mode = True
    