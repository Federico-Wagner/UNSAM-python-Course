#  6.12
from informe_funciones6q11 import leer_camion
def costo_camion(aux):
    camion = leer_camion(aux)
    sumador_valor = 0
    for line in camion:
        sumador_valor += int(line[1]) * float(line[2])
    return (sumador_valor)

costo = costo_camion('Data/camion.csv')
print('Costo total:', costo)

