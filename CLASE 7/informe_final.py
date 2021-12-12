# FUNCION MAIN 7.2
# Lista de diccionarios 2.16   (INFORME.PY)

def leer_camion(nombre_archivo):
    import csv
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    next(rows)  # Saco los headders
    camion = []
    for line in rows:
       camion.append({'nombre':line[0],'cajones':line[1],'precio':line[2]})
    f.close()
    return (0)

#7.7 ///START///
from fileparse import parse_csv

def leer_camion(aux):
    """
    Modificacion de la funcion "leer_CAMION" para que al llamar a la funcion "parce_csv" envie a la
    misma una variable de un tipo que sea iterable (f) en vez de la direccion del archivo.
    """
    with open(aux) as f:
        datos = parse_csv(f, select=['nombre','cajones','precio'],types=[str, int, float])
    lista=[]
    for row in datos:
        lista.append([row['nombre'],row['cajones'],row['precio']])
    return lista

def leer_precios(archivo):
    """
    Modificacion de la funcion "leer_precios" para que al llamar a la funcion "parce_csv" envie a la
    misma una variable de un tipo que sea iterable (f) en vez de la direccion del archivo.
    """
    with open(archivo) as f:
        return parse_csv(f,types=[str, int, float],has_headers = False,select = None)
#print(leer_precios('Data/precios.csv'))  #Dejo esto a modo de debug rapido de esta funcion

#7.7 ///END///

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


#7.5 ///START///
def main(A,B,C):
    imprimir_informe(hacer_informe(leer_camion(B)))

if __name__ == '__main__':
    main('informe_final.py','Data/camion.csv', 'Data/precios.csv')

#7.5 ///END///