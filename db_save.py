# coding=utf-8

# 1 - imports
import xlsxwriter

# 2 - extract a session
from planet.PlanetDao import PlanetDao
planetDao = PlanetDao()
planets = planetDao.getAll()

def dbSave():

    workbook = xlsxwriter.Workbook('Excel_DB/DB_Save.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, 'Planet')
    worksheet.write(0, 1, 'Gewicht')
    worksheet.write(0, 2, 'Monde')

    row = 1; col = 0

    for planet in planets:
        worksheet.write(row, col, planet.name)
        worksheet.write(row, col+1, planet.weight)

        if planet.moons:
            moons = ""
            for moonObj in planet.moons:
                moons += moonObj.name + ";"

            worksheet.write(row, col+2, moons)
        row += 1

    workbook.close()
    return
