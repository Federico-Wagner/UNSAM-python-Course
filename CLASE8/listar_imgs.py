#8.5 Recorrer el árbol de archivos

if __name__ == '__main__':
    """
    Funcion principal: Detecta todos los archivos .png que de alojen un un determinado directorio/sub-directorio,
    ingresado como parametro por consola la ruta del directorio a analizar    
    """
    import os
    import sys
    ruta = str(sys.argv[1])
    extencion = ".png"
    for root, dirs, files in os.walk(ruta):
        for name in files:
            if extencion == name[-4:]:
                print(os.path.join(name))