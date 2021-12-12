# Funciones de la biblioteca 2.9

def costo_camion(aux):
    import csv
    camion = open(aux, 'rt')
    rows = csv.reader(camion)
    next(rows)  # Saco los headders
    sumador_valor = 0
    for line in rows:
        try:
            row = line
            #print(row)
            a = int(row[1])
            b = float(row[2])
            sumador_valor = sumador_valor + a * b
        except ValueError:
            print('warning')
    camion.close()
    return (sumador_valor)

costo = costo_camion('Data/camion.csv')
print('Costo total:', costo)