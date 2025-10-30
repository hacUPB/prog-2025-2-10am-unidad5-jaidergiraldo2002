'''import matplotlib.pyplot as plt
import numpy as np
import math
# Datos
#x = np.linspace(0, 10, 100)
#y = np.sin(x)
x = []
y = []
for i in range(100):
    x.append(i)
for j in range(len(x)):
    y.append(math.cos(x[j]))


# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de coseno')
plt.xlabel('X')
plt.ylabel('cos(X)')

# Mostrar la gráfica
plt.show()


import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]

# Crear la gráfica de dispersión
plt.scatter(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Dispersión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

# Mostrar la gráfica
plt.show()

import matplotlib.pyplot as plt

# Datos
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Crear la gráfica de barras
plt.bar(categorias, valores, color="green")

# Agregar título y etiquetas
plt.title('Gráfica de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar la gráfica
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Datos
data = np.random.randn(1000)

# Crear el histograma
plt.hist(data, bins=30, edgecolor='black')

# Agregar título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()

'''
