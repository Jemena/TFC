import sqlite3
import json

DATAFILE = 'paint.json'

con = sqlite3.connect('paint.db')
cursor = con.cursor()

cursor.executescript('''DROP TABLE IF EXISTS pixels; CREATE TABLE pixels (Id PRIMARY KEY, colores)''')

with open(DATAFILE, 'r') as json_file:
    json_data = json.load(json_file)

#No quitar los comentarios o no funcionara el paint, ya que la database no funciona
#for index, colores in enumerate(json_data):
#for index, colores in zip(range(len(json_data)), json_data):
    #valor = {'id':index,'color': colores}
    #print(valor)
    #print(index, colores)
    #cursor.execute("INSERT INTO pixels values(?)",colores)
    #con.commit()
    #for color in colores:
        #valor = {'id':index, 'color': color}
        #print(valor)
        #print(index, color)
        #cursor.execute("INSERT INTO pixels values(?)", [color])



def saving(datos, destino = DATAFILE):
    with open(destino, 'w') as saved_data:
        json.dump(datos, saved_data)
    print('Saving')



