from typing import List

from base import Session
from planet.PlanetModel import Planet


class PlanetDao:

    def __init__(self):
        self.__session = Session()

    def __del__(self):
        self.__session.close()

    def insert(self, planet):
        """
        :type planet: PlanetModel
        """
        self.__session.add(planet)
        self.__session.commit()

    def getAll(self) -> List[Planet]:
        return self.__session.query(Planet).all()

    def get(self, planetId):
        """

        :type planetId: int
        """
        return self.__session.query(Planet).filter(Planet.id == planetId)
