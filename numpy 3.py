#taller Numpy
#Numpy: Biblioteca para realizar calculos numericos en 
# arreglos n-dimensiones

import numpy as np

# crear un ndarray de 2 dimensiones a partir de una lista

A = np.array ([[1,5], [1,3]])
B = np.array ([[2,0],[1,3]])

# producto punto entre ndarrays

C = np.dot (A,B)

print (C)

# Solucion de un sistema de ecuaciones con Numpy
m_solucion=np.array([5,17])

m= np.linalg.solve (A,m_solucion)

print (m)

