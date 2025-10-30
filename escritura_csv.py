import csv

a = ['Ocupacion', "Hobbies","etnia"]
b = ["Ingeniero", "futbol", "Indigena"]
c = ["Doctor", "Video juegos", "Afro"]

with open('C:\\Users\\B09S202est\\Documents\\Jaider Giraldo\\Unidad 5\\prog-2025-2-10am-unidad5-jaidergiraldo2002\\archivos\\salida.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])
    escritor.writerow(" ")
    escritor.writerow(a)
    escritor.writerow(b)
    escritor.writerow(c)
