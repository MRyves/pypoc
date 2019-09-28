from sqlalchemy import Column, String, Integer, Date, ForeignKey

from base import Base


class Moon(Base):
    __tablename__ = 'moon'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    def __init__(self, name):
        self.name = name
