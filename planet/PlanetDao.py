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

    # delete a planet by giving a planet as argument
    def delete(self, planet):
        self.__session.delete(planet)
        self.__session.commit()

    # delete a planet by giving an id as argument
    def delete1(self, planet_id):
        planet1 = self.get(planet_id)
        self.delete(planet1[0])

    #funktioniert noch nicht, wenn planet monde hat
    def delete_all(self):
        planets = PlanetDao.getAll(self)
        for planet in planets:
            self.delete1(planet.id)

    def getAll(self) -> List[Planet]:
        return self.__session.query(Planet).all()

    def get(self, planetId) -> List[Planet]:
        """

        :type planetId: int
        """
        return self.__session.query(Planet).filter(Planet.id == planetId)
