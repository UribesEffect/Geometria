#pip install matplotlib numpy imageio

import matplotlib.pyplot as plt
import numpy as np
import imageio

# Definimos los vértices del triángulo escaleno ABC
A = np.array([2, 3])
B = np.array([4, 3])
C = np.array([3, 5])

# Definimos el centro de homotecia O y la razón de homotecia k
O = np.array([0, 0])
k = 1.5

# Creamos una serie de imágenes para el GIF
images = []
for i in range(100):
    ki = 1 + i * (k - 1) / 99  # Interpolamos entre 1 y k

    # Aplicamos la homotecia para obtener los vértices del triángulo A'B'C'
    A_ = O + ki * (A - O)
    B_ = O + ki * (B - O)
    C_ = O + ki * (C - O)

    # Dibujamos los triángulos ABC y A'B'C'
    plt.figure()
    plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', label='ABC')
    plt.plot([A_[0], B_[0], C_[0], A_[0]], [A_[1], B_[1], C_[1], A_[1]], 'r-', label="A'B'C'")
    
    # Dibujamos las líneas que conectan los puntos correspondientes y se extienden hasta el infinito
    plt.plot([A[0], A_[0] + 10 * (A_[0] - A[0])], [A[1], A_[1] + 10 * (A_[1] - A[1])], 'g--')
    plt.plot([B[0], B_[0] + 10 * (B_[0] - B[0])], [B[1], B_[1] + 10 * (B_[1] - B[1])], 'g--')
    plt.plot([C[0], C_[0] + 10 * (C_[0] - C[0])], [C[1], C_[1] + 10 * (C_[1] - C[1])], 'g--')

    plt.legend()
    plt.grid(True)
    plt.xlim(2, 7)  # Ajustamos los límites del gráfico para visualizar mejor las líneas extendidas
    plt.ylim(2.5, 8)
    plt.savefig('cuadro_{:03d}.png'.format(i))  # Guardamos la imagen
    plt.close()

    # Añadimos la imagen a la lista de imágenes
    images.append(imageio.imread('cuadro_{:03d}.png'.format(i)))

# Creamos el GIF
imageio.mimsave('homotecia_con_lineas_final.gif', images)
