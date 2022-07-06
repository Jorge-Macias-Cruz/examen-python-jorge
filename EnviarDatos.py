from ObtenerDatos import obtenerDatos
import requests

def enviarDatos():
    try:
        dataSet = obtenerDatos("archivos/Clientes.txt");
        for i in dataSet:
            employee = {"firstname" : i[0], "surname" : i[1],
                        "country" : {"name" : i[2],
                        "airports" : [{"name": i[4]}]},
                        "likedLanguages": [{"name" : i[3]}]}
            resp = requests.post("http://localhost:8080/employee/apiv1/clientes/add", json=employee)
            print("Petición realizada con éxito.")
            print(resp)
            print(resp.json())
    except requests.exceptions.RequestException as e:
        print("Error en la petición: {}".format(e))