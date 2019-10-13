# coding=utf-8

# 1 - imports

# 2 - extract a session
from planet.PlanetDao import PlanetDao

planetDao = PlanetDao()
planets = planetDao.getAll()

def dbPrint():
    for planet in planets:
        print(f'Planet {planet.id}: {planet.name}')
        for moonObj in planet.moons:
            print(f'\tMoon {moonObj.id}: {moonObj.name}')
            
    return
