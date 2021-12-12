#UNIDAD 7 EJERCICIO 7.10 Caminatas al azar
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()

N = 10000
caminata_max = [0]
caminata_min = [N]

plt.subplots(figsize=(10, 6), dpi=80)
plt.subplot(2, 1, 1) # define la figura central superior
plt.ylabel('Distancia al origen')
plt.xlabel('Tiempo')
plt.suptitle('12 caminatas al azar')
plt.xticks([]), plt.yticks([])


for a in range(12):
    current = randomwalk(N)
    plt.plot(current)
    if max(abs(current)) > max(caminata_max):
        caminata_max = current
    if max(abs(current)) < max(caminata_min):
        caminata_min = current

plt.subplot(2, 2, 3) # define la figura de abajo a la izq
plt.plot(caminata_max)
plt.subplot(2, 2, 3).set_title('Caminata que mas se aleja')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4) # define la figura de abajo a la der
plt.plot(caminata_min)
plt.subplot(2, 2, 4).set_title('Caminata  que menos se aleja')
plt.xticks([]), plt.yticks([])

plt.show()