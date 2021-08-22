from settings import *
import sqlite3
import json


con = sqlite3.connect('paint.db')
cursor = con.cursor()

cursor.executescript('''DROP TABLE IF EXISTS pixels; CREATE TABLE pixels (Id integer, RGB INTEGER)''')
con.commit()

with open(DATAFILE, 'r') as json_file:
    json_data = json.load(json_file)

#print(json_data[0][1])

#No quitar los comentarios o no funcionara el paint, ya que la database no funciona
for index, colores in enumerate(json_data):
#for index, colores in zip(range(len(json_data)), json_data):
    index=str(index)
    #valor = {'id':index,'color': colores}
    #print(valor)
    #colores = str(colores) 
    #colores=json_data
    #colores=str(colores)
    #print(type(colores))
    #print(colores)
    #cursor.executemany('INSERT INTO pixels values(?)', index)
    #con.commit()
    for color in colores:
        valor = {'id':index, 'color': color}
        print(valor)
        #color = bool(color)
        #print(index, color)
        cursor.execute("INSERT INTO pixels values(?,?)", valor['id'], valor['color'])
        con.commit()





