# coding=utf-8

# 1 - import dependencies
from monde import Moon
import pandas as pd

# 2 - extract a session
from planet.PlanetDao import PlanetDao
from planet.PlanetModel import Planet

planetDao = PlanetDao()
planets = planetDao.getAll()

# 3 - write in DB
def dbSetup(Filename):

    #import database entries from excel file
    PlanetList = pd.read_excel(Filename)
    PlanetList = PlanetList[['Planet', 'Gewicht', 'Monde']].dropna(how='all').values

    #Iterate over all planets
    for i in range(0, len(PlanetList)):
        print('Adding new planet: ' + PlanetList[i,0])
        new_planet = Planet()
        new_planet.weight = PlanetList[i,1]
        new_planet.name = PlanetList[i,0]

        moon_list = []

        if type(PlanetList[i,2]) == str:
            moon_list = PlanetList[i,2].split(';')
            moon_list = [Moon(x) for x in moon_list if x]

        new_planet.moons = moon_list

        #Insert new planet in database
        planetDao.insert(new_planet)

    return






