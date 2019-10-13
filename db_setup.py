# coding=utf-8

# 1 - import dependencies
from monde import Moon
import pandas as pd

# 2 - import database entries from excel file
PlanetList = pd.read_excel("Planet_List.xlsx")
PlanetList = PlanetList[['Planet', 'Gewicht', 'Monde']].dropna(how='all').values

# 3 - extract a session
from planet.PlanetDao import PlanetDao
from planet.PlanetModel import Planet

planetDao = PlanetDao()
planets = planetDao.getAll()

# 4 - write in DB
def dbSetup():
    #Iterate over all planets
    for i in range(0, len(PlanetList)):
        print('Adding new planet: ' + PlanetList[i,0])
        new_planet = Planet()
        new_planet.weight = PlanetList[i,1]
        new_planet.name = PlanetList[i,0]
        moon_list = []

        if type(PlanetList[i,2]) == str:
            moon_list1 = PlanetList[i,2].split(';')
            #Iterate over all moons
            for j in range(len(moon_list1)):
                moon_list.append(Moon(moon_list1[j]))

        new_planet.moons = moon_list

        #Insert new planet in database
        planetDao.insert(new_planet)

    return






