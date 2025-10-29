import os
import csv
import matplotlib.pyplot as plt
import math

# --------------------------
# FUNCIONES GENERALES
# --------------------------
def listar_archivos():
    ruta = input("Ingrese una ruta (o presione Enter para usar la ruta actual): ")
    if ruta == "":
        ruta = os.getcwd()
    try:
        archivos = os.listdir(ruta)
        print("\nArchivos en la ruta seleccionada:\n")
        for archivo in archivos:
            print("-", archivo)
    except FileNotFoundError:
        print("Ruta no encontrada.")

# --------------------------
# FUNCIONES PARA ARCHIVOS .TXT
# --------------------------
def contar_palabras_y_caracteres(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
        palabras = texto.split()
        caracteres = len(texto)
        sin_espacios = len(texto.replace(" ", ""))
        print(f"\nPalabras: {len(palabras)}")
        print(f"Caracteres (con espacios): {caracteres}")
        print(f"Caracteres (sin espacios): {sin_espacios}")

def reemplazar_palabra(nombre_archivo):
    palabra_vieja = input("Palabra a reemplazar: ")
    palabra_nueva = input("Nueva palabra: ")
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    nuevo_texto = texto.replace(palabra_vieja, palabra_nueva)
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(nuevo_texto)
    print("✅ Reemplazo completado.")

def histograma_vocales(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower()
    vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for letra in texto:
        if letra in vocales:
            vocales[letra] += 1
    plt.bar(vocales.keys(), vocales.values(), color='skyblue')
    plt.title("Histograma de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Frecuencia")
    plt.show()

# --------------------------
# FUNCIONES PARA ARCHIVOS .CSV
# --------------------------
def mostrar_csv(nombre_archivo):
    with open(nombre_archivo, newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for i, fila in enumerate(lector):
            if i < 15:
                print(fila)
            else:
                break

def calcular_estadisticas(nombre_archivo):
    columna = input("Ingrese el nombre de la columna: ")
    with open(nombre_archivo, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        datos = []
        for fila in lector:
            try:
                datos.append(float(fila[columna]))
            except ValueError:
                continue

    if len(datos) == 0:
        print("Columna inválida o sin datos numéricos.")
        return

    # Cálculo manual de estadísticas
    n = len(datos)
    suma = 0
    for valor in datos:
        suma += valor
    promedio = suma / n

    datos_ordenados = sorted(datos)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    suma_diferencias = 0
    for valor in datos:
        suma_diferencias += (valor - promedio) ** 2
    desviacion = math.sqrt(suma_diferencias / (n - 1))

    maximo = max(datos)
    minimo = min(datos)

    print(f"\nNúmero de datos: {n}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")
    print(f"Máximo: {maximo:.2f}")
    print(f"Mínimo: {minimo:.2f}")

def graficar_columna(nombre_archivo):
    columna = input("Ingrese el nombre de la columna numérica a graficar: ")
    with open(nombre_archivo, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        datos = []
        for fila in lector:
            try:
                datos.append(float(fila[columna]))
            except ValueError:
                continue

    if len(datos) == 0:
        print("Columna inválida o sin datos numéricos.")
        return

    plt.scatter(range(len(datos)), datos, color='orange')
    plt.title(f"Gráfica de dispersión - {columna}")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.show()

    # Gráfico de barras ordenado
    datos_ordenados = sorted(datos)
    plt.bar(range(len(datos_ordenados)), datos_ordenados, color='green')
    plt.title(f"Gráfico de barras - {columna} ordenada")
    plt.xlabel("Índice ordenado")
    plt.ylabel("Valor")
    plt.show()

# --------------------------
# MENÚS
# --------------------------
def menu_txt():
    nombre = input("Ingrese el nombre del archivo .txt: ")
    if not os.path.exists(nombre):
        print("Archivo no encontrado.")
        return
    while True:
        print("\n--- SUBMENÚ .TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            contar_palabras_y_caracteres(nombre)
        elif opcion == "2":
            reemplazar_palabra(nombre)
        elif opcion == "3":
            histograma_vocales(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_csv():
    nombre = input("Ingrese el nombre del archivo .csv: ")
    if not os.path.exists(nombre):
        print("Archivo no encontrado.")
        return
    while True:
        print("\n--- SUBMENÚ .CSV ---")
        print("1. Mostrar primeras 15 filas")
        print("2. Calcular estadísticas")
        print("3. Graficar columna")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_csv(nombre)
        elif opcion == "2":
            calcular_estadisticas(nombre)
        elif opcion == "3":
            graficar_columna(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# --------------------------
# MENÚ PRINCIPAL
# --------------------------
def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar archivos")
        print("2. Procesar archivo .txt")
        print("3. Procesar archivo .csv")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            menu_txt()
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
