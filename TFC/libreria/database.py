from settings import *
import sqlite3
import json


con = sqlite3.connect('paint.db')
cursor = con.cursor()

cursor.executescript('''DROP TABLE IF EXISTS pixels; CREATE TABLE pixels (Id integer, RGB text)''')
con.commit()

with open(DATAFILE, 'r') as json_file:
    json_data = json.load(json_file)

#print(json_data[0][1])

#No quitar los comentarios o no funcionara el paint, ya que la database no funciona
for index, colores in enumerate(json_data):
#for index, colores in zip(range(len(json_data)), json_data):
    #valor = {'id':index,'color': colores}
    #print(valor)
    #colores = str(colores)
    index=str(index) 
    #colores=json_data
    #colores=str(colores)
    #print(type(colores))
    #print(colores)
    #cursor.executemany('INSERT INTO pixels values(?,?)', index, colores)
    #con.commit()
    for color in colores:
        #valor = {'id':index, 'color': color}
        #print(valor)
        print(index, color)
        cursor.execute("INSERT INTO pixels values(?,?)", index, color)
        con.commint()





