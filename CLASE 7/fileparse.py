#UNIDAD 7  EJERCICIO 7.4
#UNIDAD 7  EJERCICIO 7.1
# fileparse.py
import csv
def parse_csv(f,select = ['nombre','cajones','precio'],types=[str, int, float],has_headers = True,silence_errors = False):
    #Parsea una variable iterable en una lista de registros
    if(select != None and has_headers == False):
       raise RuntimeError("Para seleccionar, necesito encabezados.")
    rows = csv.reader(f)
    # Lee los encabezados
    nlinea=0
    if has_headers == True:
        headers = next(rows)
        nlinea += 1
    registros = []
    for row in rows:
        nlinea += 1
        if not row:    # Saltea filas sin datos
            continue
        try:
            if has_headers == True:
                registro = dict(zip(headers, row))
                guarda = {}
                for tipo, campo in enumerate(select):
                    guarda[campo] = types[tipo](registro[campo])
                registros.append(guarda)
            else:
                guarda2=(row[0],row[1])
                registros.append(guarda2)
        except ValueError as err:
            if silence_errors == False:
                print('error en la fila:',nlinea,', de contenido:',row,'Motivo:',err)
    #print(registros)
    return registros

#UNIDAD 7
#parse_csv('Data/precios.csv', select = ['nombre','precio'], has_headers = False)
#camion = parse_csv('Data/missing.csv', types = [str, int, float],silence_errors = True)


