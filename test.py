from sqlalchemy import Column, String, Integer, Date

from base import Base


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
