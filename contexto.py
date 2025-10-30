nombre_archivo = "./archivos/texto.txt"
with open(nombre_archivo, "r", encoding ="utf-8") as archivo:
    lista = archivo.readlines()
    # Hacer operaciones con el archivo
# El archivo se cierra automáticamente al salir del bloque with

for c in lista:
    print(c)
