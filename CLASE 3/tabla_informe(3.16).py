# AGREGAR ENCABEZADOS 3.15
import csv
def buscar_precio (aux5):
    camion2 = open('Data/precios.csv', 'rt')
    next(camion2)  # Saco los headders
    encontrado = False
    for line in camion2:
        row = line.split(',')
        a = row[0]
        if  aux5 in a:
            encontrado = True
            #print('El precio de un cajón de',aux,'es:',row[2])
            return(row[2])
    if encontrado == False:
        #print(aux,'no figura en el listado de precios.')
        return (0)
    camion2.close()

def leer_camion(aux1):
    camion = open(aux1, 'rt')
    rows1 = csv.reader(camion)
    info_camion = []
    next(rows1)
    for line in rows1:
        info_camion.append(line)
    camion.close()
    return info_camion

def hacer_informe(aux3):
    tabla = []
    contenido = []
    for lin in aux3:
        contenido = (lin[0],float(lin[1]),float(buscar_precio(lin[0])),round(float(buscar_precio(lin[0]))-float(lin[2]),2))
        tabla.append(contenido)
    return tabla

camion1 = leer_camion('Data/camion.csv')
informe = hacer_informe(camion1)

headers = ('Nombre','Cajones','Precio','Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
espacio = '-'*6
print(f'{espacio:>10s} {espacio:>10s} {espacio:>10s} {espacio:>10s}')
for r in informe:
    r = (r[0],r[1],'$'+str(r[2]),r[3],)
    print('%10s %10d %10.6s %10.2f' % r)
