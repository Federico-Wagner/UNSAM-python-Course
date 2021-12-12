import random
import numpy as np
# 5.10
def crear_album(figus_total):
    album = np.zeros(figus_total)
    #print(album)
    return album
# 5.11
def album_incompleto(album):
    return (album.min() == 0)
# 5.12
def comprar_figu(figus_total):
    return random.randint(1,figus_total)
# 5.13 - 5.16 mod (paquete de 5 figuritas)
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    figuritas = []
    while(album_incompleto(album))== True:
        for i in range(5):
            album[comprar_figu(figus_total)-1] +=1
        #print(album)
    return sum(album)
#5.17
def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append(comprar_figu(figus_total))
    return paquete
#5.18
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cantidad_paquetes = 0
    while (album_incompleto(album)) == True:
        pack = comprar_paquete(figus_total, figus_paquete)
        cantidad_paquetes +=1
        for i in pack:
            album[i - 1] += 1
    return cantidad_paquetes

# 5.14-
# 5.15
figus_total = 670
n_repeticiones = 100
cantidad_FIGS = []


for i in range(n_repeticiones):
    cantidad_FIGS.append(cuantas_figus(figus_total))
print('el promedio de figuritas para llenar el albun de',figus_total,'figuritas es de:', (np.mean(cantidad_FIGS)))


#5.19
cantidad_PACK = []
figus_paquete = 5
for i in range(n_repeticiones):
    cantidad_PACK.append(cuantos_paquetes(figus_total, figus_paquete))
print('el promedio de PAQUETES de figuritas para llenar el albun de', figus_total, 'figuritas es de:', (np.mean(cantidad_PACK)))

import matplotlib.pyplot as plt

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()




