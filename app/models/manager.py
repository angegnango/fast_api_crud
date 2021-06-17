from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base, engine
from sqlalchemy.orm import relationship

class Manager(Base):

    __tablename__ = "managers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String)
    

