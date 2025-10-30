import csv

with open("C:\\Users\\B09S202est\\Documents\\Jaider Giraldo\\Unidad 5\\prog-2025-2-10am-unidad5-jaidergiraldo2002\\archivos" + "\\Variables.csv", "r") as csvfile:
#usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    print(lector)
    encabezado = next(lector)
    encabezado = next(lector)
    encabezado = next(lector)
    presion = []
    print(encabezado[0])
    for fila in lector:              #con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace(",", ".")
        dato = float(fila[3])
        presion.append(dato)

print(presion)
