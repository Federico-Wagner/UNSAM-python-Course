#3.17 TABLA DE MULTIPLICAR
headers = ['','0','1','2','3','4','5','6','7','8','9']
print(f'{headers[0]:^10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}{headers[4]:>10s} {headers[5]:>10s} {headers[6]:>10s} {headers[7]:>10s}{headers[8]:>10s} {headers[9]:>10s} {headers[10]:>10s}')
espacio = '-'*120
print(espacio)
for n in range(10):
    headers = [str(n)+':',0,n,2*n,3*n,4*n,5*n,6*n,7*n,8*n,9*n]
    print(f'{headers[0]:^10s} {headers[1]:>10d} {headers[2]:>10d} {headers[3]:>10d}{headers[4]:>10d} {headers[5]:>10d} {headers[6]:>10d} {headers[7]:>10d}{headers[8]:>10d} {headers[9]:>10d} {headers[10]:>10d}')