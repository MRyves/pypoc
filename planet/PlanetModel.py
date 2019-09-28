from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship

from base import Base


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    weight = Column('gewicht', Integer)
    moons = relationship('Moon')
