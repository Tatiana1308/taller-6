import numpy as np
#Matplotlib tiene muchos modulos, importar uno solo
import matplotlib.pyplot as plt

# dubujar una funcion seno
#Crear un ndarray de 1 una dimension, 100 elementos equiespaciados, de 0 a 2*PI

X=np.linspace(0, 2*np.pi, 100)

Y=np.sin(X)

# Usar matplotlib

plt.figure(figsize=(8,4))
plt.title("Mi primer grafico cientifico en programacion")
plt.plot(X,Y)
plt.xlabel("X")
plt.ylabel("seno de x")
plt.grid(True)
plt.show()
