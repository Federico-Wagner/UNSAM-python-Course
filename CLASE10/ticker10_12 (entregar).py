#10.12 El pipeline ensamblado
#10.15 Codigo simple

from vigilante import vigilar
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def ticker(camion_file, log_file, fmt):
    import informe
    import formato_tabla
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)

    tabla = formato_tabla.crear_formateador(fmt)
    tabla.encabezado(['Nombre', 'Precio', 'Cantidad'])
    if fmt == 'txt':
        for fila in filas:
            a = fila
            tabla.fila(fila.values())
    elif fmt == 'csv':
        for fila in filas:
            pr = (fila['nombre'],str(fila['precio']),str(fila['volumen']))
            tabla.fila(pr)

if __name__ == '__main__':
    ticker('Data/camion.csv', 'Data/mercadolog.csv','txt')


