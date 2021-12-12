#geringoso.py
cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
     if c == 'a' or c == 'e' or c == 'i'or c == 'o' or c == 'u'or c == 'A' or c == 'E'or c == 'I' or c == 'O' or c == 'U':
          capadepenapa = capadepenapa + c +'p'+ c.lower()
     else:
          capadepenapa = capadepenapa + c

print(capadepenapa)
