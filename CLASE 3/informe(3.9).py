"""
import csv

camion = open('Data/camion.csv', 'rt')
filas = csv.reader(camion)
encabezados = next(filas)  # Saeparo los headders
fila = next(filas)

print(list(zip(encabezados,fila)))
print(dict(zip(encabezados,fila)))
"""


# costo_camion.py
import csv
def costo_camion(nombre_archivo):
    costo_total=0
    camion = open(nombre_archivo, 'rt')
    filas = csv.reader(camion)
    encabezados = next(filas)  # Saeparo los headders

    for n_fila, fila in enumerate(filas, start=1):
        #print(encabezados)
        #print(fila)
        #for n in zip(encabezados, fila):
        #   print(n)
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    print(costo_total)


costo_camion('Data/camion.csv')
costo_camion('Data/fechas.csv')