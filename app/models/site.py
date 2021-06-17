from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base, engine
from sqlalchemy.orm import relationship
from app.models.manager import Manager


class Site(Base):

    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    nominal_electric_power = Column(Integer)
    manager_id = Column(Integer, ForeignKey("managers.id"))
    assets = relationship("Asset", back_populates="site")

