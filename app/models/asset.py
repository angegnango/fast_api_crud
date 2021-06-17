from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base, engine
from sqlalchemy.orm import relationship
from app.models.site import Site


class Asset(Base):

    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    asset_type = Column(String)
    nominal_electric_power = Column(Integer)
    site_id = Column(Integer, ForeignKey("sites.id"))
    site = relationship("Site", back_populates="assets")
