# coding=utf-8

# 1 - imports
from db_setup import dbSetup
from db_print import dbPrint
from db_save import dbSave

from user.UserDao import UserDao, User
from planet.PlanetDao import PlanetDao, Planet


# 2 - database manipulation

#Initialise the database up from Planet_List.xlsx
#dbSetup()

#Print all planets and moons
#dbPrint()

#delete one planet in db
planetDao = PlanetDao()
#planet1 = planetDao.get(10)[0]

#print(f'Planet {planet1.id}: {planet1.name}')

#planetDao.delete1(4)
#planetDao.delete_all()
erde = planetDao.get(4)
print(erde[0].moons[0].id)

#funktioniert nicht weil monde gelöscht werden
planetDao.delete1(erde[0].moons[0].id)


UserDao = UserDao()


users = UserDao.getAll()

for user in users:
        print(f'User {user.id}: {user.name}')

