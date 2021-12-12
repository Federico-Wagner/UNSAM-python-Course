# Lista de diccionarios 2.16

def leer_camion(nombre_archivo):
    import csv
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    next(rows)  # Saco los headders
    camion = []

    for line in rows:
       camion.append({'nombre':line[0],'cajones':line[1],'precio':line[2]})
    f.close()

    print(camion)
    print(camion[1])
    print(camion[1]['precio'])
    return (0)

leer_camion('Data/camion.csv')
