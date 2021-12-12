# BUSCAR PRECIO EN CAMION DE FRUTA 2.7

def buscar_precio (aux):
    camion = open('Data/precios.csv', 'rt')
    next(camion)  # Saco los headders
    encontrado = False
    for line in camion:
        row = line.split(',')
        a = row[0]
        if  aux in a:
            encontrado = True
            print('El precio de un cajón de',aux,'es:',row[2])
            return(row[2])
    if encontrado == False:
        print(aux,'no figura en el listado de precios.')
        return (0)
    camion.close()

buscar_precio('Naranja')
buscar_precio('Frambuesa')