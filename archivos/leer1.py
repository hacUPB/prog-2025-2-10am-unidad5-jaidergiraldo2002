'''archivo = open("./archivos/texto1.txt", "r")
datos = archivo.read(5)
print(datos)
datos = archivo.read(5)
archivo.close()
'''
archivo = open("./archivos/texto1.txt", "r")
# archivo.readline()
# archivo.readline()
# archivo.read(11)

archivo.seek(10)
datos = archivo.readline()
archivo.close
print(datos)
