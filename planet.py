from sqlalchemy import Column, String, Integer, Date

from base import Base


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    gewicht = Column('gewicht', Integer)


