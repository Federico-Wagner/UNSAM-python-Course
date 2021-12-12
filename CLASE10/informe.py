# informe.py  ver 9.8

import fileparse
import lote
import formato_tabla
from camion import Camion
import sys
#%%
#9.4 Usá tu clase
def leer_camion(nom_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.
    '''
    with open(nom_archivo) as lines:
        camion_dicts = fileparse.parse_csv(lines, select=['nombre','cajones','precio'], types=[str,int,float]) #Lista de diccionarios
        ret = Camion([lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts])
        return ret

def leer_precios(nom_archivo):
    '''
    Lee un archivo CSV con data de precios 
    y lo devuelve como un diccionario
    con claves nombres y con sus precios como valores
    '''
    with open(nom_archivo) as lines:
        return dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))
#%%
def hacer_informe(camion, precios):
    '''
    Crea una lista de tuplas (nombre, cajones, precio, cambio) 
    dada una lista de lotes en un camión y un diccionario de precios nuevos.
    '''
    filas = []
    for c in camion:
        precio_orig = int(c.precio)
        cambio = precios[c.nombre] - precio_orig
        reg = (c.nombre, c.cajones, precio_orig, cambio)
        filas.append(reg)
    return filas
#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])

    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)

#%%
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    #formateador = formato_tabla.FormatoTablaHTML()
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

#%%
def main():
    #sys.argv()
    informe_camion('Data/camion.csv', 'Data/precios.csv',fmt = 'txt')

if __name__ == "__main__":
    main()

