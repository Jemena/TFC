import json
import os

DATAFILE = "paint.txt"


def almacenar_datos(datos, destino=DATAFILE):
    try:
        saved_data = open(destino, 'w')
    except:
        print("No se puede abrir el fichero")
        return False
    
    print("Fichero abierto")

    try:
        saved_data.write(datos)
    except:
        print("ERROR:No se puede guardar")
        return False

    saved_data.close()
    print("Salvado")
    return True
    

def leer_datos(DATAFILE):
    try:
        saved_data = open(DATAFILE)
    except:
        print("No se puede abrir el archivo")
        return False
    
    print("Fichero abierto")
    
    try:
        datos = json.load(saved_data, 'r')
    except:
        print("ERROR:No se puede abrir")
        return False

    saved_data.close()
    return None


def actualizar_datos(datos, destino=DATAFILE):
    return almacenar_datos(datos=datos, destino=destino )


def borrar_datos(destino=DATAFILE):
    try:
        os.remove(destino)
    except:
        print("No he podido borrar")
        return False

    print("Ok, borrado")
    return True