# Balances 2.18
#camion.csv  precios pagados al productor de frutas
#precios.csv  precios de venta en el lugar de descarga del camión

import csv

# BUSCAR PRECIO EN CAMION DE FRUTA 2.7

def buscar_precio (aux):
    camion2 = open('Data/precios.csv', 'rt')
    next(camion2)  # Saco los headders
    encontrado = False
    for line in camion2:
        row = line.split(',')
        a = row[0]
        if  aux in a:
            encontrado = True
            #print('El precio de un cajón de',aux,'es:',row[2])
            return(row[2])
    if encontrado == False:
        #print(aux,'no figura en el listado de precios.')
        return (0)
    camion2.close()


def BALANCE():
    camion = open('Data/camion.csv', 'rt')
    rows = csv.reader(camion)
    next(rows)                                  # Saco los headders
    facturacion = 0.0
    costo_total = 0.0
    for line in rows:
        row = line
        d = row[0]
        #print('FRUTA:', d)                              #FRUTA

        a = float(row[1])                               #cantidad de cajones
        b = float(row[2])                               #costo del cajon
        c = buscar_precio(str(row[0]))                  #precio de venta
        costo_total = costo_total + a * b               #costo
        facturacion = facturacion + (a * float(c))      #facturacion

        #print('FRUTA:', d)                              #FRUTA
        # print('valor de venta', c)                     #precio de venta
        #print('costo cajon', b)                         #costo del cajon
        #print('cant cajones',a)                         #cantidad de cajones

    print('costo total', costo_total)
    print('facturacion', facturacion)
    camion.close()
    return (round(facturacion - costo_total,2))

print('margen total:', BALANCE())


