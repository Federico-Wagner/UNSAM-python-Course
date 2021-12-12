#8.1 Segundos vividos

def segundos_vividos(fecha):
    from datetime import datetime
    fecha_splited = fecha.split("/")
    hoy = datetime.now()
    fecha_formateada = datetime(int(fecha_splited[2]), int(fecha_splited[1]), int(fecha_splited[0]))
    delta = hoy - fecha_formateada
    return delta.total_seconds()

print(segundos_vividos("19/03/1994"))