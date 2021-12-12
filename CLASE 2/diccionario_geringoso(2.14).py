#geringoso.py
diccionario = {}

def traductor (a):
    capadepenapa = ''
    lista = a
    for h in range(len(lista)):
        #print (lista[h])
        for c in lista[h]:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                capadepenapa = capadepenapa + c + 'p' + c.lower()
            else:
                capadepenapa = capadepenapa + c
        diccionario[lista[h]] = capadepenapa
        capadepenapa = ''

traductor(['banana', 'manzana', 'mandarina'])

print (diccionario)