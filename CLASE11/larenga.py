#11.9 Pascal
def pascal(n,k):
	if (k==0 or k==n): #Paso base extremos igual a 1
		return 1
	else:#Paso recursivo calcula valores superiores
		return (pascal(n-1,k-1)+pascal(n-1,k))
