# coding=utf-8

# 1 - imports
from base import Session
from monde import Moon

# 2 - extract a session
from planet.PlanetDao import PlanetDao
from planet.PlanetModel import Planet

planetDao = PlanetDao()
planets = planetDao.getAll()

for planet in planets:
    print(f'Planet {planet.id}: {planet.name}')
    for moonObj in planet.moons:
        print(f'\tMoon {moonObj.id}: {moonObj.name}')

print('Adding new planet: Earth')
earth = Planet()
earth.weight = 100
earth.name = 'earth'
earth.moons = [Moon('earth-moon')]

