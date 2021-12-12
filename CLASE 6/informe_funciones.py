# AGREGAR ENCABEZADOS 3.15
import csv
from fileparse import parse_csv

def leer_camion(aux):
    aux = parse_csv(aux, select=['nombre','cajones','precio'],types=[str, int, float])
    lista=[]
    for row in aux:
        lista.append([row['nombre'],row['cajones'],row['precio']])
    return lista

def leer_precios():
    return parse_csv('Data/precios.csv',types=[str, int, float],has_headers = False)

def buscar_precio (aux5):
    camion2 = open('Data/precios.csv', 'rt')
    next(camion2)  # Saco los headders
    encontrado = False
    for line in camion2:
        row = line.split(',')
        a = row[0]
        if aux5 in a:
            encontrado = True
            camion2.close()
            return(row[2])
    if encontrado == False:
        camion2.close()
        return (0)

def hacer_informe(aux3):
    tabla = []
    for lin in aux3:
        contenido = (lin[0],float(lin[1]),float(buscar_precio(lin[0])),round(float(buscar_precio(lin[0]))-float(lin[2]),2))
        tabla.append(contenido)
    return tabla

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    espacio = '-' * 6
    print(f'{espacio:>10s} {espacio:>10s} {espacio:>10s} {espacio:>10s}')
    for r in informe:
        r = (r[0], r[1], '$' + str(r[2]), r[3],)
        print('%10s %10d %10.6s %10.2f' % r)

imprimir_informe(hacer_informe(leer_camion('Data/camion.csv')))

