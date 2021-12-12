#11.13 HOJAS ISO
# A0 miden 841 mm de ancho y 1189 mm de largo.

def medida_rec(n):
	if n == 0:
		alto_A0 = 841
		largo_A0 = 1189

		return (alto_A0,largo_A0)
	else:
		(alto_,largo_) = medida_rec(n-1)
		(alto, largo) =(largo_//2, alto_)

		return (alto, largo)

"""
print('A0',medida_rec(0))
print('A1',medida_rec(1))
print('A2',medida_rec(2))
print('A3',medida_rec(3))
print('A4',medida_rec(4))
print('A5',medida_rec(5))
print('A6',medida_rec(6))
"""