from ObtenerDatos import obtenerDatos


def enviarDatos():
    try:
        dataSet = obtenerDatos("archivos/Clientes.txt");
        print("Guardado con exito")
    except IOError as e:
        print("Ocurrio un error". format(e))
