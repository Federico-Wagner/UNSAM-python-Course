# fileparse.py
import csv

def parse_csv(nombre_archivo,select=['nombre','cajones','precio'],types=[str, int, float],has_headers = True):
    #Parsea un archivo CSV en una lista de registros
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        # Lee los encabezados
        if has_headers == True:
            headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if has_headers == True:
                registro = dict(zip(headers, row))
                guarda = {}
                for tipo, campo in enumerate(select):
                    guarda[campo] = types[tipo](registro[campo])
                registros.append(guarda)
            else:
                guarda2=(row[0],row[1])
                registros.append(guarda2)
    return registros
"""
cajones_retenidos =parse_csv('Data/camion.csv', select=['nombre','cajones','precio'],types=[str, int, float])
print(cajones_retenidos)
cajones_retenidos =parse_csv('Data/camion.csv', select=['nombre'],types=[str, int, float])
print(cajones_retenidos)
cajones_retenidos =parse_csv('Data/camion.csv', select=['nombre','cajones',])
print(cajones_retenidos)
cajones_retenidos =parse_csv('Data/precios.csv',types=[str, int, float],has_headers = False)
print(cajones_retenidos)
"""


#//////////////////////////////VERSION DE LA CATERDRA////////////////////////////////


'''
# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None):

    #Parsea un archivo CSV en una lista de registros.
    #Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
 
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros


cajones_retenidos =parse_csv('Data/camion.csv', select=['nombre','cajones'])
print(cajones_retenidos)
  '''
