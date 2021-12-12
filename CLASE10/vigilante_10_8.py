#10.8 Configuremos un pipeline simple

import os
import time

def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        else:
            yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
"""
lines = vigilar('Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
        print(line)
"""
