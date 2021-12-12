# Contar comparaciones en la búsqueda binaria 6.20
# Búsqueda binaria 6.14
def donde_insertar(lista, x,verbose = False):
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    if len(lista) == 0:
        #print('0')
        return 0
    comps = 0               # inicializo en cero la cantidad de comparaciones
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        comps += 1  # sumo la comparación que estoy por hacer
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    #print(medio)
    #print(comps)
    return medio , comps

import random
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l
def generar_elemento(m):
    return random.randint(0, m-1)

m = 10000       #cantidad de valores disponibles para los elementos dentro de la lista
n = 100         #cantidad de numeros en lista
k = 1000        #cantidad de iteraciones

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += donde_insertar(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

import matplotlib.pyplot as plt
import numpy as np

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()