# Ejecución desde la línea de comandos con parámetros 2.10
# camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
    camion = open(nombre_archivo, 'rt')
    rows = csv.reader(camion)
    next(rows)  # Saco los headders
    costo = 0
    for line in rows:
        try:
            row = line
            # print(row)
            a = int(row[1])
            b = float(row[2])
            costo = costo + a * b
        except ValueError:
            print('warning')
    return (costo)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/29-04-21/PycharmProjects/Curso UNSAM/CLASE 2/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)