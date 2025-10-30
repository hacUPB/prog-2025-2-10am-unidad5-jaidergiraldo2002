# 1. Abrir el archivo y definir el modo
archivo = open("./archivos/texto.txt", "r")
# 2. Leer el archivo
# datos = archivo.read()
#for i in range(5):
#    datos = archivo.readline()
#for datos in archivo:
#    print(datos[0])
datos = archivo.readlines()
print(datos)
# 3. Cerrar el archivo
archivo.close()
