# coding=utf-8

# 1 - imports
from base import Session
from monde import Moon
from db_setup import dbSetup
from db_print import dbPrint

#Initialise the database up from Planet_List.xlsx
dbSetup()

#Print all planets and moons
dbPrint()
