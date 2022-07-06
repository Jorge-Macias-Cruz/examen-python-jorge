import os

def obtenerDatos(path):
    try:
        file = open(path)
        dataSet = []
        for linea in file:
            valores = linea.strip().split(",")
            dataSet.append(valores)
        file.close()
        print("Guardado con exito")
        return dataSet
    except IOError as e:
        print("No se encontro el archivo {}".format(e))