# coding=utf-8

# 1 - imports
from base import Session
from planet import Planet

# 2 - extract a session
session = Session()

# 3 - extract all movies
planeten = session.query(Planet).all()

for planet in planeten:
    print(f'Plaent {planet.id}: {planet.name}')
