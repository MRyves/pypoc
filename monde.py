from sqlalchemy import Column, String, Integer, Date

from base import Base

class Monde(Base):
    __tablename__ = 'monde'
    id = Column(Integer, primary_key=True)
    name = Column ('name', String(32))
    planet_id = Column('planet_id', Integer)