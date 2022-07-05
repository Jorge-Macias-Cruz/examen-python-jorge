# file="archivos/Clientes.txt"

""" with open("archivos/Clientes.txt", "r") as f:
    valores = []
    for linea in f:
        valores.append([int(x) for x in linea.split(",")])
    print(valores) """



""" datos3 = []
with open("archivos/Clientes.txt") as fname:
	for lineas in fname:
		datos3.append(lineas.split())
print (datos3)
print ("***") """


print ("+++ 1 ++++")
datos = []
with open("archivos/Clientes.txt") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
print (datos)
print ("+++")