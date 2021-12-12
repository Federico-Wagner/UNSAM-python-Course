#ARBOLES 3.24

import csv
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