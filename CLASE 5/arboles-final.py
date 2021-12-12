#ARBOLES 4.18 con el extra

import csv
def leer_arboles(archivo):
    base_datos=open(archivo,encoding="utf-8")
    filas = csv.reader(base_datos)
    encabezados = next(filas)
    arboleda = []
    for fila in filas:
        arbol = {a: b for a,b in zip(encabezados,fila)}
        arboleda.append(arbol)
    #print(arboleda)
    return arboleda

def medidas_de_especies(especies,arboleda):
    dict = {a:[[float(arbol['altura_tot']),float(arbol['diametro'])] for arbol in arboleda if arbol['nombre_com'] == a] for a in especies}
    #for a in especies:
    #    H=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == a]
    #    dict[a] = H
    #print(dict)
    return dict

nombre_archivo = 'Data/arbolado.csv'
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


#5.25
import os.path
import matplotlib.pyplot as plt

nombre_archivo = 'Data/arbolado.csv'
os.path.join('/', 'Data','/', 'arbolado.csv')
#arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos,bins=100)
plt.show()


#5.26
arboleda = leer_arboles('Data/arbolado.csv')
H=[[float(arbol['altura_tot']),float(arbol['diametro'])] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

import numpy as np
import matplotlib.pyplot as plt

f = np.array(H)
d = f[0:,1]
h = f[0:,0]
N = 3255
colors = np.random.rand(N)
area = (100 * np.random.rand(N))  # 0 to 15 point radii
plt.scatter(d, h, s= area, c=colors, alpha=0.8)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
plt.show()


#5.27
import os
import matplotlib.pyplot as plt
import numpy as np

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
medidas = medidas_de_especies(especies, arboleda)

def graficar(especie):
        vector = medidas[especie]
        f = np.array(vector)
        alt = np.array(f[0:,0])
        diam = np.array(f[0:,1])
        plt.scatter(diam,alt,label = especie)

for especie in especies:
    graficar(especie)

#parametros de graficos
plt.legend(loc='upper left')
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title('Relación diámetro-alto')
plt.xlim(0, 200)
plt.ylim(0, 70)

plt.show()















































"""
def leer_parque(archivo,aux):
    base_datos=open(archivo,encoding="utf-8")
    filas = csv.reader(base_datos)
    encabezados = next(filas)
    lista_arboles = []
    for fila in filas:
        diccionario = dict(zip(encabezados,fila))
        if diccionario['espacio_ve'] in aux:
            lista_arboles.append(diccionario)
    especies(lista_arboles)
    contar_ejemplares(lista_arboles)
    return lista_arboles
    
def especies(aux2):
    resultados = []
    for fila in aux2:
        resultados.append(fila['nombre_com'])
    resultados2 = set(resultados)
    #print(resultados2)
    return resultados2

def contar_ejemplares(aux3):
    from collections import Counter
    tenencias = Counter()
    for s in aux3:
        tenencias[s['nombre_com']] += float(1)
    #print(tenencias)
    print(tenencias.most_common(5))
    return tenencias

def obtener_alturas(lista_arboles, especie):
    alturas = []
    cantidad = 0
    for fila in lista_arboles:
        if especie == fila['nombre_com']:
            alturas.append(float(fila['altura_tot']))
            cantidad += 1
    print('Altura maxima de los',especie,'es:',max(alturas),'metros')
    print('Altura promedio de los',especie,'es:',round((sum(alturas)/cantidad),2),'metros')
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for fila in lista_arboles:
        if especie == fila['nombre_com']:
            inclinaciones.append(float(fila['inclinacio']))
    print('Inclinacion',inclinaciones)
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    masinclinado = {'inclinacio': 0}
    for fila in lista_arboles:
        if float(fila['inclinacio']) > float(masinclinado['inclinacio']):
            masinclinado = fila
    print(masinclinado['nombre_com'],':',masinclinado['inclinacio']+'°')

def especie_promedio_mas_inclinada(lista_arboles):
    incl_prom_max = 0
    esp_target = 'error'
    from collections import Counter
    tenencias = Counter()
    acum_inclin = Counter()
    for linea in lista_arboles:
        tenencias[linea['nombre_com']] += float(1)
        acum_inclin[linea['nombre_com']] += float(linea['inclinacio'])
    print(tenencias)
    print(acum_inclin)
    for especie in tenencias:
        #print(especie)
        inc_prom = float(acum_inclin[especie])/float(tenencias[especie])
        if inc_prom > incl_prom_max:
            incl_prom_max = inc_prom
            esp_target = especie
        #print(especie,round(inc_prom,2))
    print('-'*10,'Especie con promedio de mayor inclinacion','-'*10)
    print(f'{esp_target:^30s} {incl_prom_max:^30f}')

    return tenencias


a = leer_parque('Data/arbolado.csv','GENERAL PAZ')
obtener_alturas(a, 'Jacarandá')
obtener_inclinaciones(a,'Jacarandá')
especimen_mas_inclinado(a)
especie_promedio_mas_inclinada(a)
print(' ')
a = leer_parque('Data/arbolado.csv','ANDES, LOS')
obtener_alturas(a, 'Jacarandá')
obtener_inclinaciones(a,'Jacarandá')
especimen_mas_inclinado(a)
especie_promedio_mas_inclinada(a)
print(' ')
a = leer_parque('Data/arbolado.csv','CENTENARIO')
obtener_alturas(a, 'Jacarandá')
obtener_inclinaciones(a,'Jacarandá')
especimen_mas_inclinado(a)
especie_promedio_mas_inclinada(a)

"""