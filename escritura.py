ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
#\ se usa para comandos de texto
nombre_archivo = "frutas2.txt"
'''modo = "w" # Solo escritura - sobrescribe'''
'''modo = "a" # Escribe sin sobrescribir'''
modo = "x" # Crea un archivo nuevo, NO existente
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding="utf-8")
frase = input("Por favor ingresa una frase: ")
fp.write(frase+"\n")
#solicitar una variable entera y una flotante al usuario
#escribirla en el archivo
identificacion = int(input("Ingresa tu ID: "))
altura = float(input("Ingrese su estatura: "))
fp.write(str(identificacion))
fp.write("\n")
fp.write(str(altura))
fp.write("\n")

fp.close()